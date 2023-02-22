/*
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "FakeGPS.h"
#include <stdlib.h>
#include "MySocketExample.h"
#include <string>
#include <iostream>

#define ADDRESS "127.0.0.1"
#define PORT 64209

FakeGPS::FakeGPS()
{
    sock.set_blocking(false);
    sock.reuseaddress();


    // bind the socket
    if (!sock.bind(ADDRESS, PORT)) {
        std::cout << "[VisualNavigator] " << "failed to bind with "
                  << ADDRESS << ":" << PORT << std::endl;
    }
    std::cout << "[VisualNavigator] " << "flight dynamics model at "
              << ADDRESS << ":" << PORT << std::endl;

    _singleton = this;
}


// update state. This should be called often from the main loop
void FakeGPS::update()
{
        auto recvSize = sock.recv(&data, sizeof(FakeGPSLocation), 1 /*wait ms*/);


        // drain the socket in the case we're backed up
        int counter = 0;
        while (true) {
            FakeGPSLocation last_data;
            auto recvSize_last = sock.recv(&last_data, sizeof(FakeGPSLocation), 0ul);
            if (recvSize_last == -1) {
            std::cout << "[FakeGPS] " << "Drained n packets: " << counter << std::endl;
            }
            counter++;
            data = last_data;
            recvSize = recvSize_last;
        }
        if (counter > 0) {
            std::cout << "[FakeGPS] " << "Drained n packets: " << counter << std::endl;
        }

        // debug: inspect SITL packet
        std::cout << "recv " << recvSize << " bytes from " << ADDRESS << ":" << PORT << "\n";
        std::cout << "speedD: " << data.speedD << "\n";
        std::cout << "speedE: " << data.speedE << "\n";
        std::cout << "speedN: " << data.speedN << "\n";
        std::cout << "longitude: " << data.longitude << "\n";
        std::cout << "latitude: " << data.latitude << "\n";
        std::cout << "altitude: " << data.altitude << "\n";


}


// singleton instance
FakeGPS *FakeGPS::_singleton;

namespace AP
{

FakeGPS *fake_gps()
{
    return FakeGPS::get_singleton();
}

}