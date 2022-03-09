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

    notify('success', 'impression en cours...', 2000)

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
        console.log(response, response == false);

        if (response == false) {
          notify('danger', '<p>Une erreur est survenue, <br>nous n\'avons pas pu imprimer le document</p>')
        } else {
          notify('success', '<p>Merci pour votre intérêt&nbsp;!</p><p>Vous venez d\'imprimer :</p><p>' + response + '</p>')
        }
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
    filters.forEach(filter => {
      if (filter == event.target) {
        filter.classList.add('is-active');
      } else {
        filter.classList.remove('is-active');
      }
    })
    items.forEach(item => {
      if(item.getAttribute("data-category").includes(category)) {
        item.classList.add('is-active');
      } else {
        item.classList.remove('is-active');
      }
    })
  })
})

// -----------------------------------------------------------------
// -- Déclenche une notification
// -- ex d'utilisation :  
//      <button onclick="notify('success', 'Vous avez débloqué...');">notification</button>
//      <div data-notif data-notif-type="success">Texte de la notif</div>
// ---------------
// -- La notification ne peut être appelée que sur une page contenant :
// -- "<div class="toast-center" role="log"></div>"
// -- Cette div ne peut être ajoutée en JS
// -- autrement elle ne sera pas détectée par les lecteurs d'écran.

function destroyNotification(element, wrapper) {
  element.classList.add("is-leaving");

  element.addEventListener("animationend", () => {
    wrapper.removeChild(element);
  });
}

function notify(type, message, length = 6000) {
  const notificationLog = document.querySelector(".toast-center");
  const notif = document.createElement("aside");
  notif.classList.add("toast", `toast--${type}`)
  notif.innerHTML = message;

  notificationLog.appendChild(notif);

  console.log(notif);

  setTimeout(() => {
    destroyNotification(notif, notificationLog)
  }, length);
}