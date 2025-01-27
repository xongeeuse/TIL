package com.example.osmprac.location


import android.content.Context
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import android.os.Bundle

class LocationTracker(
    private val context: Context,
    private val onLocationUpdate: (Location) -> Unit
) {
    private val locationManager = context.getSystemService(Context.LOCATION_SERVICE) as LocationManager

    private val locationListener = object : LocationListener {
        override fun onLocationChanged(location: Location) {
            onLocationUpdate(location)
        }

        override fun onStatusChanged(provider: String?, status: Int, extras: Bundle?) {}
        override fun onProviderEnabled(provider: String) {}
        override fun onProviderDisabled(provider: String) {}
    }

    // 위치 업데이트 시작
    fun startTracking() {
        try {
            locationManager.requestLocationUpdates(
                LocationManager.GPS_PROVIDER,
                5000L, // 5초마다 업데이트
                10f,   // 10미터 이상 이동 시 업데이트
                locationListener
            )
        } catch (e: SecurityException) {
            e.printStackTrace()
        }
    }

    // 위치 업데이트 중지
    fun stopTracking() {
        locationManager.removeUpdates(locationListener)
    }
}