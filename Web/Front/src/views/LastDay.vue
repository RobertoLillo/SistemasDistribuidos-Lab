<template>
  <v-main>
    <v-container class="mb-5">
      <v-row justify="center">
        <h1
          class="montserrat-font color-back font-weight-medium display-2 pb-5 mb-4"
        >
          Datos del Ultimo día
        </h1>
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
export default {
  data() {
    return {
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
  methods: {
    getColor(calories) {
      if (calories > 400) return "red";
      else if (calories > 200) return "orange";
      else return "green";
    },
  },
};
</script>

<style>
</style>