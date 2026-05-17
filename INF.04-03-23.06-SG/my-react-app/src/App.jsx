import 'bootstrap/dist/css/bootstrap.css'

function App() {
  function formularzFunkcja() {
    const tytul = document.getElementById("filmTitle").value;
    const rodzaj = document.getElementById("variation").options[document.getElementById("variation").value].text;
    console.log("tytul: " + tytul + "; rodzaj: " + rodzaj);
  }

  return (
    <>
      <form action="">
        <div className="form-group">
          <label htmlFor="filmTitle">Tytuł filmu</label>
          <input id="filmTitle" type="text" className="form-control" />
        </div>
        <div className="form-group">
          <label htmlFor="variation">Rodzaj</label>
          <select id="variation" type="text" className="form-control">
            <option value=""></option>
            <option value="1">Komedia</option>
            <option value="2">Obyczajowy</option>
            <option value="3">Sensacyjny</option>
            <option value="4">Horror</option>
          </select>
        </div>
        <button type="button" className="btn btn-primary" onClick={formularzFunkcja}>Dodaj</button>
      </form>
    </>
  )
}

export default App