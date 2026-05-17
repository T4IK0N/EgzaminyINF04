import { useState } from 'react'
import 'bootstrap/dist/css/bootstrap.css'
import './App.css'

function App() {
  const [kursy, setKursy] = useState([
    "Programowanie w C#",
    "Angular dla początkujących",
    "Kurs Django"
  ])

  function funkcja(event) {
    event.preventDefault();
    console.log(document.getElementById("imieNazwisko").value);
    const numer = document.getElementById("numerKursu").value;
    if (numer <= kursy.length && numer >= 1) {
      console.log(kursy[numer-1]);
    } else {
      console.log("Nieprawidłowy numer kursu");
    }
  }

  return (
    <>
      <h2>Liczba kursów: {kursy.length}</h2>
      <ol>
        {
          kursy.map((element, index) =>
            <li key={index}>{element}</li>
          )
        }
      </ol>
      <form>
        <div className="form-group">
          <label htmlFor="imieNazwisko">Imię i nazwisko</label>
          <input className="form-control" type="text" name="imieNazwisko" id="imieNazwisko" />
        </div>
        <div className="form-group">
          <label htmlFor="numerKursu">Numer kursu</label>
          <input className="form-control" type="text" name="numerKursu" id="numerKursu" />
        </div>
        <button className="btn btn-success" type="submit" onClick={(event) => {funkcja(event)}}>Zapisz do kursu</button>
      </form>
    </>
  )
}

export default App
