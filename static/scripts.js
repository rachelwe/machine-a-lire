/**
 * 
 * @param {Object} parameters 
 * @param {HTMLElement} parameters.node
 * @param {string} parameters.url
 * @param {Object} parameters.options
 * @param {string} parameters.options.method
 * @param {formdata} parameters.options.body
 * @param {string} parameters.options.redirect
 */
 function formSubmit(parameters) {

  parameters.url = parameters.url || "";
  parameters.options = parameters.options || {
    method: 'GET',
    redirect: 'follow'
  }

  fetch(parameters.url, parameters.options)
    .then(response => {
      if (!response.ok) {
        const placeholderCallbackError = () => {console.log(' ')}
        parameters.callbackError = parameters.callbackError || placeholderCallbackError;
        parameters.callbackError(response)
        throw new Error(response.statusText);
      }
      return response.json();
    })
    .then(output => {
      const placeholderCallback = (res) => {console.log('callback undefined, output :', res)}
      parameters.callback = parameters.callback || placeholderCallback;
      parameters.callback(output)
      console.log('request done '+parameters.url+' :', output, parameters.callback);
    })
    .catch(error => console.error(error));
}

const forms = document.querySelectorAll('form');
forms.forEach(form => {
  form.addEventListener("submit", (event) => {
    event.preventDefault();

    formSubmit({
      node: event.target,
      url: event.target.action,
      callbackError: function (error) {
        error.json()
          .then(output => {
            console.log(output);
          });
      },
      callback: function (response) {
        console.log(response);
      }
    })
  })
})

// Example fetch for the interface
// fetch('../static/random-file.json', {
//   method: 'GET'
// })
// .then(response => response.json())
// .then(data => {
//   console.log('Success:', data);
//   data.reverse();
//   const wrapper = document.querySelector('.datas')
//   data.forEach((element) => {
    
//     const item = document.createElement('li');
//     item.innerHTML = `
//       <p><strong>Date et heure : ${element.timestamp}</strong></p>
//     `;
//     wrapper.appendChild(item);
//   });
  
// })
// .catch((error) => {
//   console.error('Error:', error);
// });