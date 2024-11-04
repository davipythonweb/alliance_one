import React from 'react'
import viteLogo from '/vite.svg'

function App() {
  const [customers, setCustomers] = React.useState([]);

  React.useEffect(() => {
    const loadData =  () => {
        fetch('http://localhost:7500/api/customers/')
        .then(response => response.json())
        .then(data => setCustomers(data))
    };
    loadData();
  }, []);


  return (
    <div className='App'>
      <header className='app-header'>
        {customers.map((customer) => (
          <h1 key={customer.id}>{customer.first_name} {customer.last_name}</h1>
        ))}
      </header>
    </div>
  );
}

export default App;
