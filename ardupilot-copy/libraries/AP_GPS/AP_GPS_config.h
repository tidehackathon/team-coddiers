#pragma once

#ifndef AP_GPS_BACKEND_DEFAULT_ENABLED
#define AP_GPS_BACKEND_DEFAULT_ENABLED 1
#endif

#ifndef AP_GPS_ERB_ENABLED
  #define AP_GPS_ERB_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_GSOF_ENABLED
  #define AP_GPS_GSOF_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_NMEA_ENABLED
  #define AP_GPS_NMEA_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_NMEA_UNICORE_ENABLED
  #define AP_GPS_NMEA_UNICORE_ENABLED AP_GPS_NMEA_ENABLED
#endif

#ifndef AP_GPS_NOVA_ENABLED
  #define AP_GPS_NOVA_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_SBF_ENABLED
  #define AP_GPS_SBF_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_SBP_ENABLED
  #define AP_GPS_SBP_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_SBP2_ENABLED
   #define AP_GPS_SBP2_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_SIRF_ENABLED
  #define AP_GPS_SIRF_ENABLED AP_GPS_BACKEND_DEFAULT_ENABLED
#endif

#ifndef AP_GPS_UBLOX_ENABLED
  #define AP_GPS_UBLOX_ENABLED 1
#endif
