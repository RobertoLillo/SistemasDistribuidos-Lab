<template>
  <v-app>
    <div class="back">
      <div class="astro">
        <v-container fluid class="fill-height mx-5">
          <v-row align="center">
            <v-col cols="4">
              <h2
                class="display-2 montserrat-font pb-3 font-weight-bold"
                style="color: #f37a27"
              >
                LAB 3
              </h2>
              <h1
                class="display-3 montserrat-font font-weight-bold pb-5"
                style="color: #170d66"
              >
                EL UNIVERSO EN UN <b>STREAM</b>
              </h1>
              <subtitle-1 class="headline font-weight-light">
                Aplicación de recoplinación de datos astronomicos realizada con:
              </subtitle-1>
              <v-row class="pt-10" justify="center">
                <img
                  class="mx-4"
                  height="70px"
                  width="auto"
                  src="../assets/docker.png"
                />
                <img
                  class="mx-4"
                  height="70px"
                  width="auto"
                  src="../assets/kafka.png"
                />
                <img
                  class="mx-4"
                  height="70px"
                  width="auto"
                  src="../assets/cassandra.png"
                />
                <img
                  class="mx-4"
                  height="70px"
                  width="auto"
                  src="../assets/redis.png"
                />
              </v-row>

              <subtitle-1 class="headline font-weight-light">
                <br />
                Consultar datos :
              </subtitle-1>
              <v-row class="pt-10" justify="center">
                <v-btn
                  class="mx-3"
                  color="#0a0756"
                  elevation="8"
                  large
                  dark
                  rounded
                  @click="
                    $vuetify.goTo('#' + 'Last', { duration: 1000, offset: -50 })
                  "
                >
                  Ultimo día
                </v-btn>
          
              </v-row>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </div>
  </v-app>
</template>

<script>
export default {
  name: "Home",
};
</script>
<style scoped>
.back {
  height: 100%;
  background-image: url("../assets/back2-01.svg");
  background-color: white;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
.astro {
  height: 100%;
  background-image: url("../assets/astro-01.svg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
