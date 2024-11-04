import { useState, useEffect} from 'react'
import viteLogo from '/vite.svg'


function App() {
  const [cars, setCars] = useState([])

  useEffect (() => {
    const loadData = () => {
      fetch('http://127.0.0.1:7500/api/cars/')
      .then(response => response.json())
      .then(data => setCars(data))
    }
    loadData()
  }, [])

  return ( 
  <div className='App'>
    <header className='app-header'>

    {cars.map(car => (
      <h1 key={car.id}>{car.name} {car.brand} </h1>
    ))}
    </header>
  </div>
)
}

export default App
