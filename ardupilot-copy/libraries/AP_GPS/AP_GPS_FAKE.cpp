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

#include "AP_GPS_FAKE.h"

#if AP_FAKE_GPS_ENABLED

#include <ctype.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>

extern const AP_HAL::HAL& hal;


bool AP_GPS_FAKE::read(void)
{
    FakeGPS *fakeGps = AP::fake_gps();
    const uint32_t now = AP_HAL::millis();
    if (now - last_update_ms < 200) {
        return false;
    }
    last_update_ms = now;

    double latitude = fakeGps->data.latitude;
    double longitude = fakeGps->data.longitude;
    float altitude = fakeGps->data.altitude;
    const double speedN = fakeGps->data.speedN;
    const double speedE = fakeGps->data.speedE;
    const double speedD = fakeGps->data.speedD;


    state.time_week = 100; //some mocked unknown values
    state.time_week_ms = 1000; //some mocked unknown values
    state.status = AP_GPS::GPS_OK_FIX_3D;
    state.num_sats = 1;

    state.location = Location{
        int32_t(latitude*1e7),
        int32_t(longitude*1e7),
        int32_t(altitude*100),
        Location::AltFrame::ABSOLUTE
    };

    state.hdop = 100;
    state.vdop = 100;

    state.have_vertical_velocity = true;
    state.velocity.x = speedN;
    state.velocity.y = speedE;
    state.velocity.z = speedD;

    velocity_to_speed_course(state);

    state.have_speed_accuracy = true;
    state.have_horizontal_accuracy = true;
    state.have_vertical_accuracy = true;
    state.have_vertical_velocity = true;

    // state.horizontal_accuracy = pkt.horizontal_pos_accuracy;
    // state.vertical_accuracy = pkt.vertical_pos_accuracy;
    // state.speed_accuracy = pkt.horizontal_vel_accuracy;

    state.last_gps_time_ms = now;

    return true;
}

#endif  // AP_FAKE_GPS_ENABLED
