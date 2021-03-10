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
      <v-data-table
        :headers="headers"
        :items="days"
        class="elevation-1"
        :loading="loading"
        color="#170d66"
      >
      </v-data-table>
    </v-container>
  </v-main>
</template>

<script>
export default {
  data() {
    return {
      loading: false,
      headers: [
        {
          text: "ID",
          align: "center",
          sortable: false,
          value: "id",
        },
        { text: "Light curve", align: "center", sortable: false, value: "st" },
        { text: "Nerly Black", align: "center", sortable: false, value: "nl" },
        { text: "fecha", align: "center", sortable: false, value: "date" },
        { text: "ZTF ID", align: "center", sortable: false, value: "jd" },
      ],
      days: [],
    };
  },
  methods: {
    getColor(calories) {
      if (calories > 400) return "red";
      else if (calories > 200) return "orange";
      else return "green";
    },
  },
  mounted() {
    this.loading = true;
    setTimeout(() => {
      this.loading = false;
      console.log("Datos recibidos")
      this.days = [
        {
          id: 1,
          st: "ZTFlc20acudnrv",
          nl: "ZTF2nb1aagkeet",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 2,
          st: "ZTFlc21aagkeer",
          nl: "ZTF2nb1aagkefb",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 3,
          st: "ZTFlc17aabtpfb",
          nl: "ZTF2nb0acudnrv",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 4,
          st: "ZTFlc18acvgyvs",
          nl: "ZTF2nb1aagkeer",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 5,
          st: "ZTFlc19aafxoyj",
          nl: "ZTF1nb7aabtpfb",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 6,
          st: "ZTFlc20ackijbs",
          nl: "ZTF1nb8acvgyvs",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 7,
          st: "ZTFlc18acvgzol",
          nl: "ZTF1nb9aafxoyj",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 8,
          st: "ZTFlc18acvazem",
          nl: "ZTF2nb0ackijbs",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 9,
          st: "ZTFlc18acvgzqo",
          nl: "ZTF1nb8acvgzol",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 10,
          st: "ZTFlc17aabtoul",
          nl: "ZTF1nb8acvazem",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 11,
          st: "ZTFlc18acvgznn",
          nl: "ZTF1nb8acvgzqo",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 12,
          st: "ZTFlc20aadsxhl",
          nl: "ZTF1nb7aabtoul",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 13,
          st: "ZTFlc20aadswhz",
          nl: "ZTF1nb8acvgznn",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 14,
          st: "ZTFlc21aagkeey",
          nl: "ZTF2nb0aadsxhl",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 15,
          st: "ZTFlc19acwbgtu",
          nl: "ZTF2nb0aadswhz",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 16,
          st: "ZTFlc19ackjpbm",
          nl: "ZTF2nb1aagkeey",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 17,
          st: "ZTFlc21aagkeej",
          nl: "ZTF1nb9acwbgtu",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 18,
          st: "ZTFlc20acvaftd",
          nl: "ZTF1nb9ackjpbm",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 19,
          st: "ZTFlc21aagkeez",
          nl: "ZTF2nb1aagkeej",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 20,
          st: "ZTFlc18acvwfie",
          nl: "ZTF2nb0acvaftd",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 21,
          st: "ZTFldfghfghdfg",
          nl: "ZTF2fgfdfgdfvx",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 22,
          st: "ZTFlc19acwbgtu",
          nl: "ZTF2gfhfgdwerv",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 23,
          st: "ZTFldfgdfgdfgm",
          nl: "ZTF2fdgfger3gb",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 24,
          st: "ZTFlgdfgdfggfj",
          nl: "ZTF1nb9acwbgtu",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 25,
          st: "ZTFlc20acvaftd",
          nl: "ZTF1dfgdfgdfgm",
          date: "10-03-2021",
          jd: 2459235.0,
        },
        {
          id: 26,
          st: "ZTFldfgsrewwda",
          nl: "ZTF2nb1aafqeej",
          date: "10-03-2021",
          jd: 2459235.0,
        },
      ];
    }, 2000);
  },
};
</script>

<style>
</style>