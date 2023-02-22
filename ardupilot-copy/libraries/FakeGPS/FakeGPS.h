#pragma once

#include "MySocketExample.h"

class FakeGPS
{
public:
    FakeGPS();

    // get singleton instance
    static FakeGPS *get_singleton()
    {
        return _singleton;
    }

    // external position backend types (used by _TYPE parameter)
    struct FakeGPSLocation {
        double longitude;
        double latitude;
        float altitude;
        double speedD;
        double speedN;
        double speedE;

    };

    // update state of all beacons
    void update();

    FakeGPSLocation data = FakeGPSLocation();

private:
    MySocketExample sock = MySocketExample(true);

    static FakeGPS *_singleton;


    FakeGPSLocation beacon_state;

};

namespace AP
{
FakeGPS *fake_gps();
};



