package com.example.schroniskostyczen2026

import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.RadioButton
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val pytania = arrayOf("Które to schronisko?", "Zwierzę na zdjęciu to", "W oddali są widoczne")
        val odpowiedzi1 = arrayOf("Na Rysiance.", "Na Wielkiej Raczy.", "Na Wielkiej Rycerzowej.")
        val odpowiedzi2 = arrayOf("owczarek.", "wilk.", "kozica.")
        val odpowiedzi3 = arrayOf("Himalaje.", "Alpy.", "Tatry.")

        val radio1: RadioButton = findViewById(R.id.radio1)
        val radio2: RadioButton = findViewById(R.id.radio2)
        val radio3: RadioButton = findViewById(R.id.radio3)
        val imageView: ImageView = findViewById(R.id.imageView)
        val textView: TextView = findViewById(R.id.textView)

        var page = 2
        var points = 0

        findViewById<Button>(R.id.button).setOnClickListener {
            when (page) {
                1 -> {
                    if (radio1.isChecked) {
                        points+=1
                    }

                    radio1.isChecked = false
                    radio2.isChecked = false
                    radio3.isChecked = false

                    imageView.setImageResource(R.drawable.zad1)
                    textView.text = pytania[0]
                    radio1.text = odpowiedzi1[0]
                    radio2.text = odpowiedzi1[1]
                    radio3.text = odpowiedzi1[2]
                    page++
                }
                2 -> {
                    if (radio2.isChecked) {
                        points+=1
                    }

                    radio1.isChecked = false
                    radio2.isChecked = false
                    radio3.isChecked = false

                    imageView.setImageResource(R.drawable.zad2)
                    textView.text = pytania[1]
                    radio1.text = odpowiedzi2[0]
                    radio2.text = odpowiedzi2[1]
                    radio3.text = odpowiedzi2[2]
                    page++
                }
                3 -> {
                    if (radio1.isChecked) {
                        points+=1
                    }

                    radio1.isChecked = false
                    radio2.isChecked = false
                    radio3.isChecked = false

                    imageView.setImageResource(R.drawable.zad3)
                    textView.text = pytania[2]
                    radio1.text = odpowiedzi3[0]
                    radio2.text = odpowiedzi3[1]
                    radio3.text = odpowiedzi3[2]
                    page = 1
                }
                else -> imageView.setImageResource(R.drawable.zad1)
            }
        }
    }
}