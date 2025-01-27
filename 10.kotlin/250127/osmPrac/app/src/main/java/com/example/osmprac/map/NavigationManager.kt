package com.example.osmprac.map

import android.content.Context
import android.location.Location
import android.speech.tts.TextToSpeech
import org.osmdroid.util.GeoPoint
import java.util.Locale
import kotlin.math.atan2
import kotlin.math.cos
import kotlin.math.sin
import kotlin.math.sqrt

class NavigationManager(
    private val context: Context,
    private val map: DrawingMapView
) {
    // 내비게이션 정보를 담는 데이터 클래스
    data class NavigationInfo(
        val distance: Double,        // 다음 회전까지 남은 거리(미터)
        val direction: Float,        // 회전 각도
        val instruction: String      // 음성 안내 텍스트
    )

    private var tts: TextToSpeech? = null
    private var routePoints: List<GeoPoint> = emptyList()
    private var currentPointIndex = 0

    init {
        // TTS 초기화
        initTTS()
    }

    // TTS 초기화 함수
    private fun initTTS() {
        tts = TextToSpeech(context) { status ->
            if (status == TextToSpeech.SUCCESS) {
                // TTS 엔진 설정
                tts?.language = Locale.KOREAN
            }
        }
    }

    // 경로 설정
    fun setRoute(points: List<GeoPoint>) {
        routePoints = points
        currentPointIndex = 0
    }

    // 현재 위치 기반 내비게이션 정보 업데이트
    fun updateNavigation(currentLocation: Location): NavigationInfo? {
        if (routePoints.isEmpty()) return null

        // 다음 경유지 찾기
        val nextPoint = findNextPoint(currentLocation)
        // 거리 계산
        val distance = calculateDistance(currentLocation, nextPoint)
        // 방향 계산
        val direction = calculateDirection(currentLocation, nextPoint)
        // 안내 메시지 생성
        val instruction = generateInstruction(direction, distance)

        return NavigationInfo(distance, direction, instruction)
    }

    // 다음 경유지 찾기
    private fun findNextPoint(currentLocation: Location): GeoPoint {
        // 현재 위치에서 가장 가까운 경로 포인트 찾기
        var minDistance = Double.MAX_VALUE
        var nearestIndex = currentPointIndex

        for (i in currentPointIndex until routePoints.size) {
            val point = routePoints[i]
            val distance = calculateDistance(
                currentLocation,
                GeoPoint(point.latitude, point.longitude)
            )
            if (distance < minDistance) {
                minDistance = distance
                nearestIndex = i
            }
        }

        currentPointIndex = nearestIndex
        return routePoints[nearestIndex]
    }

    // 두 지점 간 거리 계산 (미터 단위)
    private fun calculateDistance(location: Location, point: GeoPoint): Double {
        val results = FloatArray(1)
        Location.distanceBetween(
            location.latitude, location.longitude,
            point.latitude, point.longitude,
            results
        )
        return results[0].toDouble()
    }

    // 방향 계산 (각도)
    private fun calculateDirection(location: Location, point: GeoPoint): Float {
        val lat1 = Math.toRadians(location.latitude)
        val lon1 = Math.toRadians(location.longitude)
        val lat2 = Math.toRadians(point.latitude)
        val lon2 = Math.toRadians(point.longitude)

        val dLon = lon2 - lon1
        val y = sin(dLon) * cos(lat2)
        val x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dLon)
        var bearing = atan2(y, x)
        bearing = Math.toDegrees(bearing)
        return ((bearing + 360) % 360).toFloat()
    }

    // 안내 메시지 생성
    private fun generateInstruction(direction: Float, distance: Double): String {
        val distanceText = when {
            distance < 30 -> "잠시 후"
            else -> "${distance.toInt()}미터 앞에서"
        }

        return when {
            direction in 315.0..360.0 || direction in 0.0..45.0 -> "$distanceText 직진하세요"
            direction in 45.0..135.0 -> "$distanceText 우회전하세요"
            direction in 135.0..225.0 -> "$distanceText 반대 방향입니다"
            direction in 225.0..315.0 -> "$distanceText 좌회전하세요"
            else -> "경로를 이탈했습니다"
        }
    }

    // 음성 안내 실행
    fun provideVoiceGuidance(instruction: String) {
        tts?.speak(instruction, TextToSpeech.QUEUE_FLUSH, null, null)
    }

    // 리소스 해제
    fun cleanup() {
        tts?.stop()
        tts?.shutdown()
    }
}