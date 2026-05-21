package com.example.wlasciwosciczcionki

import android.os.Bundle
import android.widget.Button
import android.widget.SeekBar
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.core.view.ViewCompat
import androidx.core.view.WindowInsetsCompat

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val seekBar = findViewById<SeekBar>(R.id.seekBar)
        val rozmiarTekst = findViewById<TextView>(R.id.rozmiarTekst)
        val napisCytatu = findViewById<TextView>(R.id.napisCytatu)

        seekBar.setOnSeekBarChangeListener(object : SeekBar.OnSeekBarChangeListener {
            override fun onProgressChanged(seekBar: SeekBar?, progress: Int, fromUser: Boolean) {
                rozmiarTekst.text = "Rozmiar: ${seekBar?.progress}"
                napisCytatu.textSize = progress.toFloat()
            }

            override fun onStartTrackingTouch(seekBar: SeekBar?) {}

            override fun onStopTrackingTouch(seekBar: SeekBar?) {}
        })

        val teksty = listOf("Dzień dobry", "Good morning", "Buenos dias")
        val button = findViewById<Button>(R.id.button)
        button.setOnClickListener {
            if (napisCytatu.text.toString() == teksty[0]) {
                napisCytatu.text = teksty[1]
            } else if (napisCytatu.text.toString() == teksty[1]) {
                napisCytatu.text = teksty[2]
            } else if (napisCytatu.text.toString() == teksty[2]) {
                napisCytatu.text = teksty[0]
            }
        }
    }
}