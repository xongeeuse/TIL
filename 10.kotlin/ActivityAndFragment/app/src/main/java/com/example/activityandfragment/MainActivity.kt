package com.example.activityandfragment

import android.content.Intent
import android.os.Bundle
import android.widget.Button
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main)) { v, insets ->
            val systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars())
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom)
            insets
        }
        settingButton()
    }

    fun settingButton() {
        // Button 빨갛게 떴을 때 alt + enter 통해서 자동 import
        val button = findViewById<Button>(R.id.button)
        button.setOnClickListener {
            // subactivity로 이동
            // intent 의지, 지향 : 나 이러이렇게 할래!
            val intent = Intent(this, SubActivity::class.java)
            startActivity(intent)
        }
    }
}