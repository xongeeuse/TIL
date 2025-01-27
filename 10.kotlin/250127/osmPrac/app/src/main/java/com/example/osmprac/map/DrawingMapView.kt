package com.example.osmprac.map

import android.content.Context
import android.graphics.Color
import android.util.AttributeSet
import android.view.MotionEvent
import org.osmdroid.views.MapView
import org.osmdroid.util.GeoPoint
import org.osmdroid.views.overlay.Polyline
import org.osmdroid.bonuspack.routing.Road
import org.osmdroid.bonuspack.routing.RoadManager  // RoadManager도 필요


class DrawingMapView @JvmOverloads constructor(
    context: Context,
    attrs: AttributeSet? = null
) : MapView(context, attrs) {

    // 현재 그리고 있는 경로를 저장할 Polyline
    private var currentPath: Polyline? = null

    // 저장된 모든 경로점들
    private val pathPoints = mutableListOf<GeoPoint>()

    // 그리기 모드 상태 - private 제거
    var isDrawingMode = false  // private 제거하고 public으로 변경
        private set  // setter는 private 유지

    init {
        // 기본 설정
        setMultiTouchControls(true)
        setBuiltInZoomControls(false)
    }

    // 그리기 모드 전환
    fun toggleDrawingMode() {
        isDrawingMode = !isDrawingMode
        if (isDrawingMode) {
            // 새로운 경로 시작
            currentPath = Polyline().apply {
                outlinePaint.color = Color.RED
                outlinePaint.strokeWidth = 5f
            }
            overlays.add(currentPath)
        }
    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        if (isDrawingMode && event != null) {
            when (event.action) {
                MotionEvent.ACTION_DOWN -> {
                    // 터치 시작 - 새로운 경로 시작
                    startNewPath(event)
                }
                MotionEvent.ACTION_MOVE -> {
                    // 터치 이동 - 경로에 점 추가
                    addPointToPath(event)
                }
                MotionEvent.ACTION_UP -> {
                    // 터치 종료 - 경로 완성
                    finishPath()
                }
            }
            return true
        }
        return super.onTouchEvent(event)
    }

    private fun startNewPath(event: MotionEvent) {
        // IGeoPoint를 GeoPoint로 변환
        val point = projection.fromPixels(event.x.toInt(), event.y.toInt())
        val geoPoint = GeoPoint(point.latitude, point.longitude)
        currentPath?.points?.clear()
        currentPath?.addPoint(geoPoint)
        pathPoints.add(geoPoint)
        invalidate()
    }

    private fun addPointToPath(event: MotionEvent) {
        // IGeoPoint를 GeoPoint로 변환
        val point = projection.fromPixels(event.x.toInt(), event.y.toInt())
        val geoPoint = GeoPoint(point.latitude, point.longitude)
        currentPath?.addPoint(geoPoint)
        pathPoints.add(geoPoint)
        invalidate()
    }

    private fun finishPath() {
        // 경로 완성 시 필요한 처리
        isDrawingMode = false
    }

    // 저장된 경로점들 반환
    fun getDrawnPath(): List<GeoPoint> = pathPoints.toList()

    private var road: Road? = null
    private var roadOverlay: Polyline? = null

    fun showRoute(calculatedRoad: Road) {
        road = calculatedRoad
        // 기존 경로 제거
        roadOverlay?.let { overlays.remove(it) }

        // 새 경로 표시
        roadOverlay = RoadManager.buildRoadOverlay(calculatedRoad, Color.BLUE, 10f)
        overlays.add(roadOverlay)
        invalidate()
    }

    fun clearRoute() {
        roadOverlay?.let { overlays.remove(it) }
        road = null
        invalidate()
    }
}