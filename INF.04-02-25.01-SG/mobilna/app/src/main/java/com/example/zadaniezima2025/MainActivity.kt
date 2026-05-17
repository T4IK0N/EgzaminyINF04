package com.example.zadaniezima2025

import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContentView(R.layout.activity_main)

        val poleEdycyjne: EditText = findViewById(R.id.poleEdycyjne)
        val przyciskPralka: Button = findViewById(R.id.przyciskPralka)
        val napisPralka: TextView = findViewById(R.id.napisPralka)

        przyciskPralka.setOnClickListener {
            val liczba = poleEdycyjne.text.toString().toIntOrNull()

            if (liczba in 1..12) {
                napisPralka.text = "Numer prania: $liczba"
            }
        }

        val odkurzaczPrzycisk: Button = findViewById(R.id.odkurzaczPrzycisk)
        val odkurzaczTekst: TextView = findViewById(R.id.odkurzaczTekst)

        odkurzaczPrzycisk.setOnClickListener {
            if (odkurzaczPrzycisk.text == "Włącz") {
                odkurzaczPrzycisk.text = "Wyłącz"
                odkurzaczTekst.text = "Odkurzacz włączony"
            } else {
                odkurzaczPrzycisk.text = "Włącz"
                odkurzaczTekst.text = "Odkurzacz wyłączony"
            }
        }
    }
}