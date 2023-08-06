#!/usr/bin/env python3
# ----------------------------------------------------------------------------
#
# Copyright 2018 EMVA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# ----------------------------------------------------------------------------


# Standard library imports
import unittest

# Related third party imports

# Local application/library specific imports
from harvesters.test.base_harvester import TestHarvesterCoreBase
from harvesters.core import ImageAcquisitionManager


class TestHarvesterCore(TestHarvesterCoreBase):

    def test_basic_usage_1(self):
        """
        We walk through a basic usage and manually close the image
        acquisition manager.

        :return: None.
        """

        # Prepare an image acquisition manager for device #0.
        iam = self._harvester.open_image_acquisition_manager(0)

        # Acquire images.
        self._basic_usage(iam)

        # Discard the image acquisition manager.
        iam.close()

    def test_basic_usage_2(self):
        """
        We walk through a basic usage and omit manually closing the image
        acquisition manager using the with statement.

        :return: None.
        """

        # Prepare an image acquisition manager for device #0.
        with self._harvester.open_image_acquisition_manager(0) as iam:

            # Acquire images.
            self._basic_usage(iam)

    @staticmethod
    def _basic_usage(iam: ImageAcquisitionManager):
        # Set up the device.
        iam.device.node_map.Width.value = 12
        iam.device.node_map.Height.value = 8
        iam.device.node_map.PixelFormat.value = 'Mono8'

        # Start image acquisition.
        iam.start_image_acquisition()

        # Fetch a buffer that is filled with image data.
        with iam.fetch_buffer_manager() as bm:
            print(bm)
            # Reshape it.
            _1d = bm.payload
            _2d = _1d.reshape(
                bm.buffer.height, bm.buffer.width
            )
            print(_2d)

        # Stop image acquisition.
        iam.stop_image_acquisition()

    def test_multiple_image_acquisition_managers(self):
        num_devices = len(self._harvester.device_info_list)
        self._test_image_acquisition_managers(num_iaas=num_devices)

    def _test_image_acquisition_managers(self, num_iaas=1):
        #
        print('Number of devices: {0}'.format(num_iaas))

        #
        iams = []  # Image Acquisition Managers

        #
        for list_index in range(num_iaas):
            iams.append(
                self._harvester.open_image_acquisition_manager(
                    list_index=list_index
                )
                # Or you could simply do the same thing as follows:
                # self._harvester.open_image_acquisition_manager(list_index)
            )

        #
        for i in range(10):
            #
            print('---> Round {0}: Set up'.format(i))
            for index, iam in enumerate(iams):
                iam.start_image_acquisition()
                print(
                    'Device #{0} has started image acquisition.'.format(index)
                )

            k = 0

            # Run it as fast as possible.
            frames = 10

            while k < frames:
                for iam in iams:
                    if k % 2 == 0:
                        # Option 1: This way is secure and preferred.
                        try:
                            # We know we've started image acquisition but this
                            # try-except block is demonstrating a case where
                            # a client called fetch_buffer method even though
                            # he'd forgotten to start image acquisition.
                            with iam.fetch_buffer_manager() as bm:
                                print(bm)
                        except AttributeError:
                            # Harvester Core has not started image acquisition
                            # so calling fetch_buffer() raises AttributeError
                            # because None object is used for the with
                            # statement.
                            pass
                    else:
                        # Option 2: You can manually do the same job but not
                        # recommended because you might forget to queue the
                        # buffer.
                        bm = iam.fetch_buffer_manager()
                        print(bm)
                        iam.queue_buffer(bm)

                #
                k += 1

            #
            print('<--- Round {0}: Tear down'.format(i))
            for index, iam in enumerate(iams):
                iam.stop_image_acquisition()
                print(
                    'Device #{0} has stopped image acquisition.'.format(index)
                )

        for iam in iams:
            iam.close()

    def test_controlling_a_specific_camera(self):
        # The basic usage.
        iam = self._harvester.open_image_acquisition_manager(0)
        iam.close()

        # The basic usage but it explicitly uses the parameter name.
        iam = self._harvester.open_image_acquisition_manager(
            list_index=0
        )
        iam.close()

        # The key can't specify a unique device so it raises an exception.
        with self.assertRaises(ValueError):
            self._harvester.open_image_acquisition_manager(
                vendor='EMVA_D'
            )

        # The key specifies a unique device.
        print(self._harvester.device_info_list)
        iam = self._harvester.open_image_acquisition_manager(
            serial_number='SN_InterfaceA_0'
        )
        iam.close()


if __name__ == '__main__':
    unittest.main()
