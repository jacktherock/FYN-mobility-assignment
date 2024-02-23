import React, { useState, useEffect } from 'react';
import axios from 'axios';
import PricingList from './components/PricingList';

const App = () => {
  const BASE_URL = 'http://127.0.0.1:8000/api'
  const [pricingConfigurations, setPricingConfigurations] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get(`${BASE_URL}/pricing_config/`);
      setPricingConfigurations(response.data);
    } catch (error) {
      console.error('Error fetching pricing configurations:', error);
    }
  };

  return (
    <div className='bg-[#EEF1FF] py-5'>
      <PricingList pricingConfigurations={pricingConfigurations} />
    </div>
  );
};

export default App;
