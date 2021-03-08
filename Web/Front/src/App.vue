<template>
  <v-app>
    <v-app-bar
      app
      :height="scrollPosition == 0 ? 120 : 70"
      class="custom-navbar px-5"
      elevate-on-scroll
      :class="[
        scrollPosition > 0
          ? 'custom-color-navbar-elevate'
          : 'custom-color-navbar',
      ]"
    >
      <v-toolbar-title>
        <h2 class="montserrat-font color-back font-weight-bold mr-4">
          <span class="text--gray">Distribuidos</span>
          <span class="font-weight-light text--gray">Lab</span>
        </h2>
      </v-toolbar-title>

      <v-spacer></v-spacer>
      <v-btn text :dark="scrollPosition == 0" class="mx-3" @click="$vuetify.goTo('#' + 'Last', options)" > ultimo día </v-btn>
      <v-btn text :dark="scrollPosition == 0" class="mx-3" @click="$vuetify.goTo('#' + 'Data', options)"> Datos guardados </v-btn>
      <v-divider vertical :dark="scrollPosition == 0" inset></v-divider>
      <v-btn text :dark="scrollPosition == 0" class="mx-3" @click="$vuetify.goTo('#' + 'Home', options)"> Inicio </v-btn>
    </v-app-bar>
    <Home id="Home"></Home>
    <Last id="Last"></Last>
    <v-divider class="mx-7"></v-divider>
    <Data id="Data"></Data>
  </v-app>
</template>

<script>
import Home from "./views/Home";
import Last from "./views/LastDay";
import Data from "./views/Data";
export default {
  name: "App",

  data: () => ({
    scrollPosition: 0,
    duration: 1000,
    offset: -50,
  }),
  computed: {
    options() {
      return {
        duration: this.duration,
        offset: this.offset,
      };
    },
  },
  methods: {
    updateScroll() {
      this.scrollPosition = window.scrollY;
    },
    updateSelector(element) {
      this.selector = "#" + element;
    },
  },
  mounted() {
    window.addEventListener("scroll", this.updateScroll);
  },

  components: {
    Home,
    Last,
    Data,
  },
};
</script>
<style scoped>
.color-transparent {
  color: rgba(0, 0, 0, 0);
}
</style>
<style>
@import url("https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,300;0,700;0,900;1,500&display=swap");

.montserrat-font {
  font-family: "Montserrat", sans-serif;
}

.color-back {
  color: #0a0756;
}

.custom-navbar {
  transition: background-color 0.5s ease-out, box-shadow 0.5s ease-out, height 0.5s ease-out !important;
}
.custom-color-navbar {
  background-color: transparent !important;
}
.custom-color-navbar-elevate {
  background-color: white !important;
  
}
</style>
