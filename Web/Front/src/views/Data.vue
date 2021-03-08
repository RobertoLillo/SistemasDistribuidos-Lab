<template>
  <v-main>
    <v-container class="mb-5">
      <v-row justify="center">
        <h1
          class="montserrat-font color-back font-weight-medium display-2 pb-5 mb-4"
        >
          Datos Historicos
        </h1>
      </v-row>
      <v-row justify="center">
        <v-col cols="12" lg="3" class="mx-3">
          <v-menu
            v-model="menu1"
            :close-on-content-click="false"
            max-width="290"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                color="#0a0756"
                :value="computeInicio"
                clearable
                label="Inicio"
                readonly
                v-bind="attrs"
                v-on="on"
                @click:clear="inicio = null"
              ></v-text-field>
            </template>
            <v-date-picker
            color="#0a0756"
              no-title
              :max="date"
              v-model="inicio"
              @change="changeIni"
            ></v-date-picker>
          </v-menu>
        </v-col>
        <v-col cols="12" lg="3" class="mx-3">
          <v-menu
           
            v-model="menu2"
            :close-on-content-click="false"
            max-width="290"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                :disabled="inicio == null"
                color="#0a0756"
                :value="computeTermino"
                clearable
                label="Termino"
                readonly
                v-bind="attrs"
                v-on="on"
                @click:clear="termino = null"
              ></v-text-field>
            </template>
            <v-date-picker
              no-title
              color="#0a0756"
              :min="inicio"
              :max="date"
              v-model="termino"
              @change="changeTer"
            ></v-date-picker>
          </v-menu>
        </v-col>
      </v-row>
      <v-data-table :headers="headers" :items="desserts" class="elevation-1">
        <template v-slot:[`item.action`]="{}">
          <v-btn color="grey darken-2 " dark class="mx-2" icon>
            <v-icon>fa-eye </v-icon>
          </v-btn>
        </template>
      </v-data-table>
    </v-container>
  </v-main>
</template>

<script>
import moment from "moment";
export default {
  data() {
    return {
      date: moment(new Date()).format("YYYY-MM-DD"),
      inicio: null,
      termino: null,
      menu1: false,
      menu2: false,
      headers: [
        {
          text: "ID",
          align: "center",
          sortable: false,
          value: "id",
        },
        { text: "Valor X", align: "center", sortable: false, value: "valueX" },
        { text: "Valor Y", align: "center", sortable: false, value: "valueY" },
        { text: "Valor Z", align: "center", sortable: false, value: "valueZ" },
        { text: "Ver", align: "center", sortable: false, value: "action" },
      ],
      desserts: [
        {
          id: 1,
          valueX: 159,
          valueY: 6.0,
          valueZ: 24,
        },
        {
          id: 2,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 3,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 4,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 5,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 6,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 7,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 8,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 9,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 10,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 11,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 12,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 13,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
        {
          id: 14,
          valueX: 451,
          valueY: 41.0,
          valueZ: 24,
        },
      ],
    };
  },
  computed: {
    computeInicio() {
      return this.inicio ? moment(this.inicio).format("DD-MM-YYYY") : "";
    },
    computeTermino() {
      return this.termino ? moment(this.termino).format("DD-MM-YYYY") : "";
    },
  },
  methods:{
      changeIni(){
          this.termino = null;
          this.menu1 = false;
      },
      changeTer(){
          this.menu2 = false;
      }
  }
};
</script>

<style>
</style>