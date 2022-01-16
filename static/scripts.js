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
      return response.text();
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
        error.text()
          .then(output => {
            console.log(output);
            alert(output);
          });
      },
      callback: function (response) {
        console.log(response);
      }
    })
  })
})

const filters = document.querySelectorAll('[data-target]');
const items = document.querySelectorAll("[data-category]");
filters.forEach(filter => {
  filter.addEventListener("click", (event) => {
    const category = event.target.getAttribute("data-target");
    if (!category) {return;}
    items.forEach(item => {
      if(item.getAttribute("data-category").includes(category)) {
        item.classList.add('is-active');
      } else {
        item.classList.remove('is-active');
      }
    })
  })
})