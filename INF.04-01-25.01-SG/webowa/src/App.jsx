import { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import './App.css';

function App() {

  const [lista, setLista] = useState([
    {id: 0, alt: "Mak", filename: "obraz1.jpg", category:1, downloads: 35},
    {id: 1, alt:"Bukiet", filename: "obraz2.jpg", category: 1, downloads: 43},
    {id: 2, alt:"Dalmatyńczyk", filename: "obraz3.jpg", category:2, downloads: 2},
    {id: 3, alt:"Świnka morska", filename: "obraz4.jpg", category:2, downloads: 53},
    {id: 4, alt:"Rotwailer", filename: "obraz5.jpg", category:2, downloads: 43},
    {id: 5, alt:"Audi", filename: "obraz6.jpg", category:3, downloads: 11},
    {id: 6, alt:"kotki", filename: "obraz7.jpg", category:2, downloads: 22},
    {id: 7, alt:"Róża", filename: "obraz8.jpg", category:1, downloads: 33},
    {id: 8, alt:"Świnka morska", filename: "obraz9.jpg", category:2, downloads: 123},
    {id: 9, alt:"Foksterier", filename: "obraz10.jpg", category:2, downloads: 22},
    {id: 10, alt:"Szczeniak", filename: "obraz11.jpg", category:2, downloads: 12},
    {id: 11, alt:"Garbus", filename: "obraz12.jpg", category:3, downloads: 321}
  ])

  const [kwiatyChecked, setKwiatyChecked] = useState(true)
  const [zwierzetaChecked, setZwierzetaChecked] = useState(true)
  const [samochodyChecked, setSamochodyChecked] = useState(true)

  function usun(id) {
    setLista(l => l.filter((value) => value.id !== id));
  }

  function dodaj() {
    const zdjecieInput = document.getElementById("zdjecie").value;
    const pobranInput = document.getElementById("pobran").value;

    const element = {
      // Generujemy ID na podstawie czasu, aby było unikalne
      id: Date.now(), 
      alt: "Nowe zdjęcie",
      // Musi być 'filename', bo tego używasz w map()
      filename: zdjecieInput, 
      // Dodajemy domyślną kategorię, żeby element nie zniknął po dodaniu
      category: 1, 
      downloads: parseInt(pobranInput) || 0,
    };

    setLista(l => [...l, element]);
    
    // Opcjonalnie: wyczyść pola po dodaniu
    document.getElementById("zdjecie").value = "";
    document.getElementById("pobran").value = "";
  }

  /*
  **********************************************
  nazwa metody: ustawPobrania
  opis metody: ustawa liczbe pobrań na +1
  parametry: index - przechowuje obecny index obiektu który trzeba zmienić
  zwracany typ i opis: brak
  autor: bogumil_gasowski
  ***********************************************
  */
  function ustawPobrania(index) {
    const nowaLista = [...lista]
    nowaLista[index].downloads += 1
    setLista(nowaLista)
  }

  return (
    <>
      <h1>Kategorie zdjęć</h1>
      <div style={{display: "flex", flexDirection: "row", gap: "10px"}}>
        <div className="form-check form-switch">
          <input onChange={() => setKwiatyChecked(k => k = !k)} className="form-check-input" type="checkbox" name="kwiaty" id="kwiaty" defaultChecked="true"/>
          <label className="form-check-label" htmlFor="kwiaty">Kwiaty</label>
        </div>
        <div className="form-check form-switch">
          <input onChange={() => setZwierzetaChecked(z => z = !z)} className="form-check-input" type="checkbox" name="zwierzeta" id="zwierzeta" defaultChecked="true"/>
          <label className="form-check-label" htmlFor="zwierzeta">Zwierzęta</label>
        </div>
        <div className="form-check form-switch">
          <input onChange={() => setSamochodyChecked(s => s = !s)} className="form-check-input" type="checkbox" name="samochody" id="samochody" defaultChecked="true"/>
          <label className="form-check-label" htmlFor="samochody">Samochody</label>
        </div>
      </div>
      <div style={{display: "grid", gridTemplateColumns: "repeat(3, 1fr)"}}>
      {
        lista.map((element, _) => {
          if (kwiatyChecked && element.category === 1 ||
            zwierzetaChecked && element.category === 2 ||
            samochodyChecked && element.category === 3
          ) {
            return <div key={element.id} className="container" onClick={() => usun(element.id)}> 
                    <img src={`/assets/${element.filename}`} alt={element.alt} style={{margin: "5px", borderRadius: "5px"}} />
                    <h4>Pobrań: {element.downloads}</h4>
                    <button onClick={() => { ustawPobrania(element.id) }} type="button" className="btn btn-success" href={element.filename}>Pobierz</button>
                  </div>
          }
        })
      }
      </div>
      <div>
        <label htmlFor="zdjecie">Zdjęcie</label>
        <input type="text" name="zdjecie" id="zdjecie" />
        <label htmlFor="pobran">Pobrań</label>
        <input type="text" name="pobran" id="pobran" />
        <button onClick={() => dodaj()}>Dodaj</button>
      </div>
    </>
  )
}

export default App
