package com.example.koscistyczen2026

import android.annotation.SuppressLint
import android.os.Bundle
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import kotlin.random.Random

class MainActivity : AppCompatActivity() {
    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val button: Button = findViewById(R.id.button)
        val textView: TextView = findViewById(R.id.textView)
        val image1: ImageView = findViewById(R.id.image1)
        val image2: ImageView = findViewById(R.id.image2)
        val image3: ImageView = findViewById(R.id.image3)
        val image4: ImageView = findViewById(R.id.image4)
        val image5: ImageView = findViewById(R.id.image5)
        val imageDostepna = BooleanArray(5) { true }
        val listaZdjec = arrayOf(image1, image2, image3, image4, image5)
        val listaKosci = arrayOf(
            R.drawable.kosc1,
            R.drawable.kosc2,
            R.drawable.kosc3,
            R.drawable.kosc4,
            R.drawable.kosc5,
            R.drawable.kosc6,
        )

        button.setOnClickListener {
            var wynik = 0
            for (i in 0..4) {
                if (imageDostepna[i]) {
                    val losowanie = Random.nextInt(1, 7)
                    listaZdjec[i].setImageResource(listaKosci[losowanie-1])
                    wynik += losowanie
                }
            }
            textView.text = wynik.toString()
        }

        for (i in 0..4) {
            listaZdjec[i].setOnClickListener {
                if (imageDostepna[i]) {
                    imageDostepna[i] = false
                    listaZdjec[i].alpha = 0.5f
                } else {
                    imageDostepna[i] = true
                    listaZdjec[i].alpha = 1f
                }
            }
        }
    }
}