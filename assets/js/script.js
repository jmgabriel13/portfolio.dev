'use strict';



// element toggle function
const elementToggleFunc = function (elem) { elem.classList.toggle("active"); }



// sidebar variables
const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");

// sidebar toggle functionality for mobile
sidebarBtn.addEventListener("click", function () { elementToggleFunc(sidebar); });

/**
 * skills toggle
 */

const toggleBtnBox = document.querySelector("[data-toggle-box]");
const toggleBtns = document.querySelectorAll("[data-toggle-btn]");
const skillsBox = document.querySelector("[data-skills-box]");

for (let i = 0; i < toggleBtns.length; i++) {
  toggleBtns[i].addEventListener("click", function () {

    elementToggleFunc(toggleBtnBox);
    for (let i = 0; i < toggleBtns.length; i++) { elementToggleFunc(toggleBtns[i]); }
    elementToggleFunc(skillsBox);

  });
}

// custom select variables
const select = document.querySelector("[data-select]");
const selectItems = document.querySelectorAll("[data-select-item]");
const selectValue = document.querySelector("[data-selecct-value]");
const filterBtn = document.querySelectorAll("[data-filter-btn]");

select.addEventListener("click", function () { elementToggleFunc(this); });

// add event in all select items
for (let i = 0; i < selectItems.length; i++) {
  selectItems[i].addEventListener("click", function () {

    let selectedValue = this.innerText.toLowerCase();
    selectValue.innerText = this.innerText;
    elementToggleFunc(select);
    filterFunc(selectedValue);

  });
}

// filter variables
const filterItems = document.querySelectorAll("[data-filter-item]");

const filterFunc = function (selectedValue) {

  for (let i = 0; i < filterItems.length; i++) {

    if (selectedValue === "all") {
      filterItems[i].classList.add("active");
    } else if (selectedValue === filterItems[i].dataset.category) {
      filterItems[i].classList.add("active");
    } else {
      filterItems[i].classList.remove("active");
    }

  }

}

// add event in all filter button items for large screen
let lastClickedBtn = filterBtn[0];

for (let i = 0; i < filterBtn.length; i++) {

  filterBtn[i].addEventListener("click", function () {

    let selectedValue = this.innerText.toLowerCase();
    selectValue.innerText = this.innerText;
    filterFunc(selectedValue);

    lastClickedBtn.classList.remove("active");
    this.classList.add("active");
    lastClickedBtn = this;

  });

}

// projects variables
const projectItem = document.querySelectorAll("[data-project-item]");
const modalContainer = document.querySelector("[data-modal-container]");
const modalCloseBtn = document.querySelector("[data-modal-close-btn]");
const overlay = document.querySelector("[data-overlay]");

// modal variable
const modalImg1 = document.querySelector("[data-modal-img-1]");
const modalImg2 = document.querySelector("[data-modal-img-2]");
const modalImg3 = document.querySelector("[data-modal-img-3]");
const modalTech = document.querySelector("[data-modal-tech]");
const modalTitle = document.querySelector("[data-modal-title]");
const modalText = document.querySelector("[data-modal-text]");
const modalLink = document.querySelector("[data-modal-link]");
const modalBtnName = document.querySelector("[data-modal-btn-name]");
const modalBtnSourceCode = document.querySelector("[data-modal-btn-source-code]");

// modal toggle function
const projectModalFunc = function () {
  modalContainer.classList.toggle("active");
  overlay.classList.toggle("active");
}


// add click event to all modal items
for (let i = 0; i < projectItem.length; i++) {

  projectItem[i].addEventListener("click", function () {

    modalImg1.src = this.querySelector("[data-project-image-1]").src;
    modalImg1.alt = this.querySelector("[data-project-image-1]").alt
    modalImg1.style = "display: block;";

    let image2 = this.querySelector("[data-project-image-2]");
    let image3 = this.querySelector("[data-project-image-3]");

    if (image2) {
      modalImg2.src = image2.src;
      modalImg2.alt = image2.alt;
      modalImg2.style = "display: block;";
    }
    else {
      modalImg2.style = "display: none;";
    }

    if (image3) {
      modalImg3.src = image3.src;
      modalImg3.alt = image3.alt;
      modalImg3.style = "display: block;";
    }
    else {
      modalImg3.style = "display: none;";
    }

    modalTitle.innerHTML = this.querySelector("[data-project-title]").innerHTML;
    modalTech.innerHTML = this.querySelector("[data-project-tech]").innerHTML;
    modalText.innerHTML = this.querySelector("[data-project-details]").innerHTML;

    let link = this.querySelector("[data-project-link]").innerHTML;
    let btnLink = this.querySelector("[data-project-btn-name]").innerHTML;
    let sourceCodeLink = this.querySelector("[data-project-btn-source-code]").innerHTML;
    modalBtnSourceCode.innerHTML = "Source Code";

    if (btnLink === "Confidential") {
      modalBtnSourceCode.setAttribute('disabled', '');
      modalBtnSourceCode.removeAttribute("href");

      modalBtnName.innerHTML = btnLink;
      modalBtnName.setAttribute('disabled', '');
    } else if (btnLink === "Under Maintenance") {
      modalBtnSourceCode.setAttribute('disabled', '');
      modalBtnSourceCode.removeAttribute("href");

      modalBtnName.innerHTML = btnLink;
      modalBtnName.setAttribute('disabled', '');
    } else {
      modalBtnSourceCode.removeAttribute('disabled');
      modalBtnSourceCode.setAttribute("href", sourceCodeLink)

      modalBtnName.innerHTML = "Live Demo";
      modalBtnName.removeAttribute('disabled');
      modalLink.action = link;
    }

    projectModalFunc();

  });

}

// add click event to modal close button
modalCloseBtn.addEventListener("click", projectModalFunc);
overlay.addEventListener("click", projectModalFunc);




// contact form variables
const form = document.querySelector("[data-form]");
const formInputs = document.querySelectorAll("[data-form-input]");
const formBtn = document.querySelector("[data-form-btn]");

// add event to all form input field
for (let i = 0; i < formInputs.length; i++) {
  formInputs[i].addEventListener("input", function () {

    // check form validation
    if (form.checkValidity()) {
      formBtn.removeAttribute("disabled");
    } else {
      formBtn.setAttribute("disabled", "");
    }

  });
}



// page navigation variables
const navigationLinks = document.querySelectorAll("[data-nav-link]");
const pages = document.querySelectorAll("[data-page]");

// add event to all nav link
for (let i = 0; i < navigationLinks.length; i++) {
  navigationLinks[i].addEventListener("click", function () {

    for (let i = 0; i < pages.length; i++) {
      if (this.innerHTML.toLowerCase() === pages[i].dataset.page) {
        pages[i].classList.add("active");
        navigationLinks[i].classList.add("active");
        window.scrollTo(0, 0);
      } else {
        pages[i].classList.remove("active");
        navigationLinks[i].classList.remove("active");
      }
    }

  });
}