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


FakeGPS::FakeGPS()
{
    _singleton = this;

}


// update state. This should be called often from the main loop
void FakeGPS::update(void)
{

}


// singleton instance
FakeGPS *FakeGPS::_singleton;

namespace AP {

FakeGPS *fake_gps()
{
    return FakeGPS::get_singleton();
}

}



// #pragma once
// #include <stdlib.h>
// // #include "SocketExample2.cpp"
// #include <string>
// #include <iostream>


// /**
//  * The Singleton class defines the `GetInstance` method that serves as an
//  * alternative to constructor and lets clients access the same instance of this
//  * class over and over.
//  */

// struct servo_packet {
//     double longitude;
//     double latitude;
//     float altitude;
//     double speedD;
//     double speedN;
//     double speedE;
// };

// class VisualNavigator
// {

// protected:

//     static VisualNavigator* visualNavigator_;
//     int connectionTimeoutCount;
//     int connectionTimeoutMaxCount = 10;
//     SocketExample2 sock = SocketExample2(true);
//     VisualNavigator()
//     {
//         sock.set_blocking(false);
//         sock.reuseaddress();


//         // bind the socket
//         if (!sock.bind("127.0.0.1", 42069)) {
//             std::cout << "[VisualNavigator] " << "failed to bind with "
//                       << "127.0.0.1" << ":" << 42069 << std::endl;
//         }
//         std::cout << "[VisualNavigator] " << "flight dynamics model at "
//                   << "127.0.0.1" << ":" << 42069 << std::endl;
//     }

// public:
//     servo_packet pkt = servo_packet();


//     VisualNavigator(VisualNavigator &other) = delete;
//     void operator=(const VisualNavigator &) = delete;
//     static VisualNavigator *get_singleton();

//     void updatePosition()
//     {
//         auto recvSize = sock.recv(&pkt, sizeof(servo_packet), 1 /*wait ms*/);


//         // drain the socket in the case we're backed up
//         int counter = 0;
//         while (true) {
//             servo_packet last_pkt;
//             auto recvSize_last = sock.recv(&last_pkt, sizeof(servo_packet), 0ul);
//             if (recvSize_last == -1) {
//                 break;
//             }
//             counter++;
//             pkt = last_pkt;
//             recvSize = recvSize_last;
//         }
//         if (counter > 0) {
//             std::cout << "[VisualNavigator] " << "Drained n packets: " << counter << std::endl;
//         }


//         // debug: inspect SITL packet
//         std::cout << "recv " << recvSize << " bytes from " << "127.0.0.1" << ":" << 42069 << "\n";
//         std::cout << "speedD: " << pkt.speedD << "\n";
//         std::cout << "speedE: " << pkt.speedE << "\n";
//         std::cout << "speedN: " << pkt.speedN << "\n";
//         std::cout << "longitude: " << pkt.longitude << "\n";
//         std::cout << "latitude: " << pkt.latitude << "\n";
//         std::cout << "altitude: " << pkt.altitude << "\n";

//     }
// };

// VisualNavigator* VisualNavigator::visualNavigator_ = nullptr;

// /**
//  * Static methods should be defined outside the class.
//  */
// VisualNavigator *VisualNavigator::get_singleton()
// {
//     /**
//      * This is a safer way to create an instance. instance = new VisualNavigator is
//      * dangeruous in case two instance threads wants to access at the same time
//      */
//     if (visualNavigator_==nullptr) {
//         visualNavigator_ = new VisualNavigator();
//     }
//     return visualNavigator_;
// }

