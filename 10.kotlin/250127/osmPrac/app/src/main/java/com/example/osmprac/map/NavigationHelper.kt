package com.example.osmprac.map

import android.location.Location
import org.osmdroid.bonuspack.routing.Road
import org.osmdroid.util.GeoPoint
import kotlin.math.min

class NavigationHelper(
    private val road: Road,
    private val onNavigationUpdate: (NavigationInfo) -> Unit
) {
    private var currentNodeIndex = 0

    data class NavigationInfo(
        val distanceToNextTurn: Double,
        val nextInstruction: String,
        val remainingDistance: Double
    )

    fun updateNavigation(currentLocation: Location) {
        val currentPoint = GeoPoint(currentLocation)
        val nodeIndex = findClosestNodeIndex(currentPoint)

        if (nodeIndex != currentNodeIndex) {
            currentNodeIndex = nodeIndex
            val navigationInfo = calculateNavigationInfo(currentPoint, nodeIndex)
            onNavigationUpdate(navigationInfo)
        }
    }

    private fun findClosestNodeIndex(currentPoint: GeoPoint): Int {
        // 현재 위치에서 가장 가까운 경로 상의 노드 찾기
        var minDistance = Double.MAX_VALUE
        var closestIndex = 0

        road.mRouteHigh.forEachIndexed { index, node ->
            val distance = currentPoint.distanceToAsDouble(node)
            if (distance < minDistance) {
                minDistance = distance
                closestIndex = index
            }
        }

        return closestIndex
    }

    private fun calculateNavigationInfo(
        currentPoint: GeoPoint,
        nodeIndex: Int
    ): NavigationInfo {
        // 다음 안내 지점까지의 거리와 안내 메시지 계산
        val nextInstruction = road.mNodes[nodeIndex].mInstructions
        val distanceToNext = road.mNodes[nodeIndex].mLength
        val remainingDistance = calculateRemainingDistance(nodeIndex)

        return NavigationInfo(
            distanceToNextTurn = distanceToNext,
            nextInstruction = nextInstruction,
            remainingDistance = remainingDistance
        )
    }

    private fun calculateRemainingDistance(fromIndex: Int): Double {
        var distance = 0.0
        for (i in fromIndex until road.mNodes.size) {
            distance += road.mNodes[i].mLength
        }
        return distance
    }
}