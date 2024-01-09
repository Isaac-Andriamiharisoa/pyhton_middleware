const axios = require('axios');

const flaskUrl = 'http://localhost:5000'

// Example GET request
axios.get(`${flaskUrl}/number/123`)
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });

// A POST request
axios.post(`${flaskUrl}/endpoint`, { message: 'extra' })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  })
