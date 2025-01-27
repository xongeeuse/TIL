package com.example.osmprac.map


import android.graphics.Color
import org.osmdroid.util.GeoPoint
import org.osmdroid.views.MapView
import org.osmdroid.views.overlay.Polyline
import org.osmdroid.views.overlay.mylocation.MyLocationNewOverlay

class MapHelper(private val mapView: MapView) {
    private val routePolyline = Polyline().apply {
        outlinePaint.color = Color.BLUE
        outlinePaint.strokeWidth = 10f
    }

    private val locationOverlay = MyLocationNewOverlay(mapView).apply {
        enableMyLocation()
        enableFollowLocation()  // enableFollowing() 대신 이렇게 수정
    }

    init {
        mapView.overlays.add(routePolyline)
        mapView.overlays.add(locationOverlay)
    }

    // 경로에 포인트 추가
    fun addRoutePoint(latitude: Double, longitude: Double) {
        val point = GeoPoint(latitude, longitude)
        routePolyline.addPoint(point)
        mapView.invalidate()
    }

    // 경로 초기화
    fun clearRoute() {
        routePolyline.points.clear()
        mapView.invalidate()
    }
}