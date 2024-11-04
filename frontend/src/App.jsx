import React from 'react'
import viteLogo from '/vite.svg'


function App() {
  const [cars, setCars] = React.useState([])

  React.useEffect (() => {
    const loadData = () => {
      fetch('http://localhost:7500/api/cars/')
      .then(response => response.json())
      .then(data => setCars(data))
    }
    loadData()
  }, [])

  return ( 
  <div className='App'>
    <header className='app-header'>
    {cars.map(car => (
      <h1 key={car.id}>{car.name} {car.brand} {car.release_date} </h1>
    ))}
    </header>
  </div>
)
}

export default App
