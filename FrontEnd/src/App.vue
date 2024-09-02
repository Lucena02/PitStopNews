<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { RouterLink, RouterView } from 'vue-router'
import {Moon, Menu } from 'lucide-vue-next'


const toggleSwitchRef = ref<HTMLInputElement | null>(null);
const currentTheme = localStorage.getItem('theme');


if (currentTheme) {
    console.log(currentTheme)
    if (currentTheme === 'dark' && toggleSwitchRef.value) {
        toggleSwitchRef.value.checked = true;
    }
}

function switchTheme(e?: Event) {
    let isDarkMode = false;

    if (e) {
        const target = e.target as HTMLInputElement;
        isDarkMode = target.checked;
    } else {
        const currentTheme = localStorage.getItem('theme');
        isDarkMode = currentTheme === 'dark';
    }

    if (isDarkMode) {
        localStorage.setItem('theme', 'dark');
        document.documentElement.style.setProperty('--backgroundColor', 'rgb(41, 41, 41)');
        document.documentElement.style.setProperty('--backgroundBox', 'rgb(84, 84, 84)');
        document.documentElement.style.setProperty('--fontColor', 'rgb(230, 230, 230)');
    } else {
        localStorage.setItem('theme', 'light');
        document.documentElement.style.setProperty('--backgroundColor', 'white');
        document.documentElement.style.setProperty('--backgroundBox', 'rgb(237, 237, 237)');
        document.documentElement.style.setProperty('--fontColor', 'black');
    }

    if (toggleSwitchRef.value) {
        toggleSwitchRef.value.checked = isDarkMode;
    }
}

onMounted(() => {
    const toggleSwitch = toggleSwitchRef.value;
    if (toggleSwitch) {
        toggleSwitch.addEventListener('change', switchTheme);
    }
    switchTheme();
});


</script>

<template>
  <div class="corpo">
    <div class="teste">


          <label class="theme-switch" for="checkbox">

            <input type="checkbox" id="checkbox" ref="toggleSwitchRef" @change="switchTheme"/>
            <div class="slider">
              <Moon class="iconLua"/>
            </div>
          </label>

    </div>
    <div class="containerTitle">
        <div class="header">Pit Stop News</div>
        <div class="subheader">Fast World Updates for Fast Busy People</div>
      </div>
    <div class="container">
      <div class="navbar">
        <nav class="nav-links">
          <div class="button-container">
            <RouterLink class="buttonT hover-underline-animation" to="/sports">Sports</RouterLink>
          </div>
          <div class="button-container">
            <RouterLink class="buttonT hover-underline-animation" to="/politics">Politics</RouterLink>
          </div>
          <div class="button-container">
            <RouterLink class="buttonT hover-underline-animation" to="/science">Science</RouterLink>
          </div>
          <div class="button-container">
            <RouterLink class="buttonT hover-underline-animation" to="/world">World</RouterLink>
          </div>
        </nav>


      </div>
    </div>
    <br>
    <Transition>
      <RouterView />
    </Transition>
    <div class="footer">
      <a href="mailto:your-email@example.com" class="aFooter">Contact me</a>
    </div>
  </div>
  
</template>


<style scoped>
* {
    margin: 0;
    height: 100%;
  }

.corpo{
  background-color: var(--backgroundColor);
  min-height: 100vh;
}

.v-enter-active,
.v-leave-active {
  transition: opacity 0.4s ease-in-out;
}

.v-enter-from,
.v-leave-to {
  opacity: 0.10;
}
    
.theme-switch {
  padding:10px;
  display: flex; /* Change from inline-block to flex */
  align-items: center; /* Center content vertically */
  justify-content: center; /* Center content horizontally */
  height: 34px;
  position: relative;
  width: 100px;
}

.theme-switch input {
  display:none;
}

.slider {
  background-color: #ccc;
  bottom: 0;
  width: 60px;
  height: 34px;
  cursor: pointer;
  position: absolute;
  transition: .4s;
  border-radius: 30px;
}

/*Bola dentro do slider*/
.slider:before {
  background-color: #fff;
  bottom: 4px;
  content: "";
  height: 26px;
  left: 4px;
  position: absolute;
  transition: .4s;
  width: 26px;
  border-radius: 50%;
}

input:checked + .slider {
  background-color: #4b4b4b;
}

input:checked + .slider:before {
  transform: translateX(26px);
}

.iconLua{
  position:absolute;
  z-index:2;
  transition: .4s;
  left: 5px;
}

input:checked + .slider .iconLua {
  transform: translateX(26px);
}




.hover-underline-animation {
  display: inline-block;
  position: relative;
}

.hover-underline-animation::after {
  content: '';
  position: absolute;
  width: 100%;
  transform: scaleX(0);
  height: 2px;
  bottom: 0;
  left: 0;
  
  background-color: var(--fontColor);
  transform-origin: bottom right;
  transition: transform 0.25s ease-out;
}

.hover-underline-animation:hover::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}

.hover-underline-animation:hover::after,
.router-link-active.hover-underline-animation::after {
  transform: scaleX(1);
  transform-origin: bottom left;
}

.cantos {
  align-self: flex-start;
}

.teste {
  height: 8vh;
  display: flex;
}
@media  (max-width: 800px) {
  .teste{
    height: 8vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .theme-switch {
    padding: 0px;
    display: flex; /* Change from inline-block to flex */
    align-items: center; /* Center content vertically */
    justify-content: center; /* Center content horizontally */
    height: 34px;
    position: relative;
    width: 100px;
  }
}


.containerTitle {
  width: 100%;
  text-align: center;
}

.horizontal-line {
  height: 1px;
  width: 100%;
  background-color: rgb(159, 159, 159);
}

.buttonT {
  border-radius: 6px;
  width: 20vw;
  text-align: center;
  color: black;
  text-decoration: none;
  font-family: Arial;
  font-weight: 600;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 30px;
  color: var(--fontColor);
}



.button-container {
  width: 20vw;
  display: flex;
  justify-content: center;
  align-items: center;
}



.container {
  margin-top: 5vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
}

@font-face {
  font-family: 'Cocogoose';
  src: url('./assets/Cocogoose-Pro-Semilight-trial.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Cocogoose-thin';
  src: url('./assets/Cocogoose-Pro-Thin-trial.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

.header {
  font-family: 'Cocogoose', sans-serif;
  font-size: clamp(24px, 4.1vw, 1000px);
  color: var(--fontColor);
}

.subheader {
  font-family: 'Cocogoose-thin';
  margin-bottom: 40px;
  font-size: clamp(8px, 1.4vw, 1000px);
  color: var(--fontColor);
}

.navbar nav {
  display: flex;
  gap: 1px;
  /* Adjust the spacing between links as needed */
}


@media  (max-width: 800px) {
  .navbar nav {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    column-gap: 15vw;
    text-decoration: none;
  }
  .buttonT{
    font-size:4vw;
    margin-bottom: 10px;
  }
}


@media  (max-width: 300px) {
  .navbar nav {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    column-gap: 15vw;
    text-decoration: none;
  }
  .buttonT{
    font-size:6vw;
    margin-bottom: 1px;
  }
}

.footer{
  margin-top:20px;
  text-align: center;
}

.aFooter{
  text-decoration: underline;
  cursor: pointer;
  font-weight: 600;
  color: var(--fontColor);
  font-family: Arial;
  font-size:20px;
}

</style>
