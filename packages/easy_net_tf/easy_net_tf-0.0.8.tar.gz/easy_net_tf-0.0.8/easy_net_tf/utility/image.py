import cv2
import numpy

from pathlib import Path


class UtilityImage:
    NORMALIZE_DEFAULT = 'default'
    NORMALIZE_EACH_CHANNEL = 'normalize each channel to [low,high]'
    NORMALIZE_ALL_CHANNEL = 'normalize all channel to [low,high]'

    @staticmethod
    def normalize(image_in, low, high, mode=NORMALIZE_DEFAULT):
        """
        
        :param image_in: 
        :param low: 
        :param high: 
        :param mode: 
        :return: 
        """
        image_out = numpy.copy(image_in)

        if mode == UtilityImage.NORMALIZE_DEFAULT:
            image_out = (image_out - 127.5) / 128

        # normalize each channel separately to [-1, 1]
        elif mode == UtilityImage.NORMALIZE_EACH_CHANNEL:
            height, width, channels = image_out.shape
            for channel in range(channels):
                maximum = numpy.max(image_out[:, :, channel])
                minimum = numpy.min(image_out[:, :, channel])
                image_out[:, :, channel] = (
                                                   (image_out[:, :, channel] - minimum) / (
                                               numpy.clip(a=maximum - minimum, a_min=1e-10, a_max=None)
                                           )
                                           ) * (high - low) + low

        # normalize all channels together to [-1, 1]
        elif mode == UtilityImage.NORMALIZE_ALL_CHANNEL:
            maximum = numpy.max(image_out)
            minimum = numpy.min(image_out)
            image_out = (
                                (image_out - minimum) / (numpy.clip(a=maximum - minimum, a_min=1e-10, a_max=None)
                                                         )
                        ) * (high - low) + low

        return image_out

    @staticmethod
    def resize(image_in, scale):
        image_out = numpy.copy(image_in)

        height, width, channels = image_out.shape
        new_height = int(height * scale)
        new_width = int(width * scale)

        image_out = cv2.resize(image_out,
                               (new_width, new_height),
                               interpolation=cv2.INTER_LINEAR)
        return image_out

    @staticmethod
    def rotate(image_in, center, angle, landmark_in=None):
        """

        :param image_in:
        :param center: rotation center
        :param landmark_in:
        :param angle:
        :return:
        """
        """
        image rotate
        """
        if image_in is None:
            return None, None

        image_out = numpy.copy(image_in)

        rotate_mat = cv2.getRotationMatrix2D(center, angle, 1)

        image_out = cv2.warpAffine(image_out, rotate_mat, (image_out.shape[1], image_out.shape[0]))

        """
        landmark rotate
        """
        if landmark_in is None:
            return image_out

        landmark_in = numpy.array(landmark_in,
                                  dtype=numpy.float32).reshape(-1, 2)
        landmark_out = list()

        for x, y in landmark_in:
            landmark_out.append(rotate_mat[0][0] * x + rotate_mat[0][1] * y + rotate_mat[0][2])
            landmark_out.append(rotate_mat[1][0] * x + rotate_mat[1][1] * y + rotate_mat[1][2])

        return image_out, landmark_out

    @staticmethod
    def horizontally_flip(image_in,
                          landmarks_in=None):
        """

        :param image_in:
        :param landmarks_in:
        :return:
        """

        """
        image flip
        """
        if image_in is None:
            print('Error: '
                  '[UtilityImage.horizontally_flip] '
                  'image_in cant be None')
            return

        image_out = numpy.copy(image_in)
        image_out = cv2.flip(image_out, 1)

        """
        landmark flip
        """
        if landmarks_in is not None:
            landmarks_out = numpy.copy(landmarks_in)
            landmarks_out = numpy.reshape(landmarks_out, [-1, 10])

            for landmark in landmarks_out:

                for i in range(10):
                    if i % 2 == 0:
                        # horizontally flip
                        landmark[i] = 1.0 - landmark[i]

                landmark[0], landmark[2] = landmark[2], landmark[0]
                landmark[1], landmark[3] = landmark[3], landmark[1]

                landmark[6], landmark[8] = landmark[8], landmark[6]
                landmark[7], landmark[9] = landmark[9], landmark[7]

            landmarks_out = numpy.reshape(landmarks_out, [-1])
        else:
            landmarks_out = None

        return image_out, landmarks_out

    @staticmethod
    def vertical_flip(image_in, landmark_in):
        if image_in is None:
            return None, None
        image_out = numpy.copy(image_in)
        image_out = cv2.flip(image_out, 0)

        for i in range(numpy.size(landmark_in)):
            if i % 2 == 1:
                # vertical flip
                landmark_in[i] = 1.0 - landmark_in[i]

        return image_out, landmark_in

    @staticmethod
    def draw_rectangle(image, boxes, color):
        """
        draw bounding boxes on image
        :param image:
        :param boxes: [x1, y1, x2, y2]
        :param color: (B, G, R)
        :return:
        """
        height, width, _ = image.shape

        boxes = numpy.reshape(boxes, [-1, 4])
        for box in boxes:
            x_1 = int(numpy.maximum(box[0], 0))
            y_1 = int(numpy.maximum(box[1], 0))
            x_2 = int(numpy.minimum(box[2], width - 1))
            y_2 = int(numpy.minimum(box[3], height - 1))

            cv2.rectangle(image,
                          (x_1, y_1),
                          (x_2, y_2),
                          color,
                          2)

        return image

    @staticmethod
    def add_coordinate(batch_image,
                       add_r,
                       normalize,
                       debug=False):
        """

        :param batch_image: a batch of images
        :param add_r: r coordinate=sqrt((x-width/2)^2+(y-height/2)^2)
        :param normalize:
        :param debug:
        :return:
        """

        """
        prepare
        """
        image_out = numpy.copy(batch_image)
        batch, height, width, channels = numpy.shape(image_out)

        """
        x coordinate
        """
        x_ones = numpy.ones(
            [batch, height],
            dtype=numpy.int32
        )

        x_ones = numpy.expand_dims(x_ones, -1)

        x_range = numpy.tile(
            numpy.expand_dims(
                numpy.arange(width),
                0
            ),
            [batch, 1]
        )

        x_range = numpy.expand_dims(x_range, 1)
        x_channel = numpy.matmul(x_ones, x_range)
        x_channel = numpy.expand_dims(x_channel, -1)

        """
        y coordinate
        """
        y_ones = numpy.ones(
            [batch, width],
            dtype=numpy.int32
        )
        y_ones = numpy.expand_dims(y_ones, 1)
        y_range = numpy.tile(
            numpy.expand_dims(
                numpy.arange(height),
                0
            ),
            [batch, 1]
        )
        y_range = numpy.expand_dims(y_range, -1)
        y_channel = numpy.matmul(y_range, y_ones)
        y_channel = numpy.expand_dims(y_channel, -1)

        """
        r coordinate
        """
        r_channel = numpy.sqrt(
            numpy.square(x_channel - (width - 1) / 2.0)
            + numpy.square(y_channel - (height - 1) / 2.0)
        )

        """
        normalize
        """
        if normalize:
            x_channel = x_channel / (width - 1.0) * 2.0 - 1.0
            y_channel = y_channel / (height - 1.0) * 2.0 - 1.0

            maximum = numpy.max(r_channel)
            minimum = numpy.min(r_channel)
            r_channel = ((r_channel - minimum) / (maximum - minimum)) * 2.0 - 1.0

        """
        concatenate
        """
        image_out = numpy.concatenate(
            (image_out, x_channel, y_channel),
            axis=-1
        )
        if add_r:
            if debug:
                print('Log: '
                      '[%s.%s] '
                      'add r coordinate.' % (UtilityImage.__name__,
                                             UtilityImage.add_coordinate.__name__))
            image_out = numpy.concatenate(
                (image_out, r_channel),
                axis=-1
            )

        return image_out

    VALID = 'VALID'
    SAME = 'SAME'

    @staticmethod
    def cut_out_rectangle(image_in,
                          rectangle,
                          size_out=None,
                          padding=VALID):
        """

        :param image_in:
        :param rectangle: [x1, y1, x2, y2]
        :param size_out: resize size
        :param padding: 'VALID': output valid image area; 'SAME': padding '0' is rectangle exceeds image
        :return:
        """

        image_copy = numpy.copy(image_in)

        if padding == UtilityImage.VALID:
            image_out = image_copy[rectangle[1]:(rectangle[3] + 1), rectangle[0]:(rectangle[2] + 1), :]

        elif padding == UtilityImage.SAME:
            height, width, channels = image_copy.shape

            x_1 = rectangle[0]
            y_1 = rectangle[1]
            x_2 = rectangle[2]
            y_2 = rectangle[3]

            m_height = y_2 - y_1 + 1
            m_width = x_2 - x_1 + 1

            if x_1 < 0:
                m_x_1 = -x_1
                x_1 = 0
            else:
                m_x_1 = 0

            if y_1 < 0:
                m_y_1 = -y_1
                y_1 = 0
            else:
                m_y_1 = 0

            if x_2 >= width:
                m_x_2 = m_width - 1 - (x_2 - (width - 1))
                x_2 = width - 1
            else:
                m_x_2 = m_width - 1

            if y_2 >= height:
                m_y_2 = m_height - 1 - (y_2 - (height - 1))
                y_2 = height - 1
            else:
                m_y_2 = m_height - 1

            # generate crop size mask
            image_out = numpy.zeros(shape=(m_height, m_width, channels))
            image_out[m_y_1:m_y_2 + 1, m_x_1:m_x_2 + 1, :] = image_copy[y_1:y_2 + 1, x_1:x_2 + 1, :]

        else:
            print('Error: '
                  '[%s.%s] '
                  'padding should be ''VALID'' or ''SAME''' % (UtilityImage.__name__,
                                                               UtilityImage.cut_out_rectangle.__name__))
            image_out = None

        if image_out is None:
            return
        elif size_out is not None \
                and size_out > 0:
            image_out = cv2.resize(image_out,
                                   (size_out, size_out),
                                   interpolation=cv2.INTER_LINEAR)
            return image_out

    @staticmethod
    def cut_out_rectangles(image_in,
                           rectangles,
                           size_out):
        """
        1.repair exceeding boxes to valid boxes, padding '0' in exceeding area
        2.resize to net input size;
        :param image_in:
        :param rectangles:
        :param size_out: resize size
        :return: a batch of resize cropped image
        """

        image_copy = numpy.copy(image_in)

        image_height, image_width, channels = image_copy.shape
        rectangles = numpy.around(rectangles).astype(numpy.int32)
        boxes_number = rectangles.shape[0]

        boxes_x_1 = rectangles[:, 0]
        boxes_y_1 = rectangles[:, 1]
        boxes_x_2 = rectangles[:, 2]
        boxes_y_2 = rectangles[:, 3]

        boxes_width = boxes_x_2 - boxes_x_1 + 1
        boxes_height = boxes_y_2 - boxes_y_1 + 1

        c_x_1 = numpy.zeros((rectangles.shape[0],), numpy.int32)
        c_y_1 = numpy.zeros((rectangles.shape[0],), numpy.int32)
        c_x_2 = boxes_width.copy() - 1
        c_y_2 = boxes_height.copy() - 1

        index = numpy.where(numpy.greater(boxes_x_2, image_width - 1))[0]
        if numpy.size(index) > 0:
            c_x_2[index] = (boxes_width[index] - 1) - (boxes_x_2[index] - (image_width - 1))
            boxes_x_2[index] = image_width - 1

        index = numpy.where(boxes_y_2 > image_height - 1)
        if numpy.size(index) > 0:
            c_y_2[index] = (boxes_height[index] - 1) - (boxes_y_2[index] - (image_height - 1))
            boxes_y_2[index] = image_height - 1

        index = numpy.where(boxes_x_1 < 0)
        if numpy.size(index) > 0:
            c_x_1[index] = 0 - boxes_x_1[index]
            boxes_x_1[index] = 0

        index = numpy.where(boxes_y_1 < 0)
        if numpy.size(index) > 0:
            c_y_1[index] = 0 - boxes_y_1[index]
            boxes_y_1[index] = 0

        images_out = numpy.zeros((boxes_number,
                                  size_out,
                                  size_out,
                                  channels),
                                 dtype=numpy.float32)

        for i in range(boxes_number):
            container = numpy.zeros((boxes_height[i],
                                     boxes_width[i],
                                     channels),
                                    dtype=numpy.float32)
            container[c_y_1[i]:c_y_2[i] + 1, c_x_1[i]:c_x_2[i] + 1, :] = image_copy[boxes_y_1[i]:boxes_y_2[i] + 1,
                                                                         boxes_x_1[i]:boxes_x_2[i] + 1, :]
            images_out[i, :, :, :] = cv2.resize(container, (size_out, size_out))

        return images_out

    @staticmethod
    def save_image(image_in,
                   category,
                   save_dir,
                   index,
                   stride,
                   landmarks=None,
                   offsets=None):
        """

        :param image_in:
        :param category: a list(negative:0, positive:1, partial:-1, landmark:-2).
        :param save_dir: directory of saving specific category
        :param index: image index
        :param stride: [images save stride, label save stride]
        :param landmarks:
        :param offsets:
        :return:
        """

        if image_in is None:
            return False

        if landmarks is not None \
                and offsets is not None:
            print('Error: landmark and offset can not be not None in the same time')
            return False

        """
        save image
        """
        image_folder = Path('%d' % int(index / stride[0]))
        image_name = '%d.jpg' % index

        image_path = save_dir / 'image' / image_folder / image_name
        image_path.parent.mkdir(parents=True, exist_ok=True)

        cv2.imwrite(filename=image_path.__str__(), img=image_in)

        """
        save labels
        """
        if landmarks is not None:
            label = ' ' + ' '.join(map(str, category)) \
                    + ' ' + ' '.join(map(str, landmarks)) + '\n'

        elif offsets is not None:
            label = ' ' + ' '.join(map(str, category)) \
                    + ' ' + ' '.join(map(str, offsets)) + '\n'

        else:
            label = ' ' + ' '.join(map(str, category)) + '\n'

        filename = 'labels-%d' % int(index / stride[1])
        file_path = save_dir / 'label' / filename
        file_path.parent.mkdir(parents=True, exist_ok=True)

        content = (image_folder / image_name).__str__() + label

        with file_path.open('a') as file:
            file.write(content)

        return True
