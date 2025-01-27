package com.example.osmprac.map

import android.content.Context
import org.osmdroid.bonuspack.routing.OSRMRoadManager
import org.osmdroid.bonuspack.routing.Road
import org.osmdroid.util.GeoPoint
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext


class RouteManager(private val context: Context) {
    private val roadManager = OSRMRoadManager(context, "OsmPrac/1.0")

    // 경로 계산 함수
    suspend fun calculateRoute(waypoints: ArrayList<GeoPoint>): Road? {
        return withContext(Dispatchers.IO) {
            try {
                roadManager.getRoad(waypoints)
            } catch (e: Exception) {
                null
            }
        }
    }

    // 보행자 모드 설정
    fun setWalkingMode() {
        roadManager.setMean(OSRMRoadManager.MEAN_BY_FOOT)
    }
}