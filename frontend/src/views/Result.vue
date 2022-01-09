<template>
  <div :class="$style.result__container">
    <div :class="$style.content">
      <div :class="$style.header">
        <h1 :class="$style.title">Prediksi Biaya Asuransi Kesehatan</h1>
      </div>
      <div :class="$style.charges">
        <p :class="$style.charges__name">
          Hallo, {{ name }}
        </p>
        <p :class="$style.charges__title">
          Berikut hasil pediksi biaya asuransi 
          dari data yang sudah diisikan
        </p>
        <div>
          <p>Biaya yang harus dibayarkan</p>
          <p>:</p>
          <p>{{ charges }}</p>
        </div>
      </div>
      <p>
        <button :class="$style.back" @click="back">Kembali</button>
      </p>
    </div>
    <div :class="$style.footer">
      <p>Created by :</p>
      <p>Arif Rahman Amrul Ghani - 13518023</p>
      <p>Faris Fadhilah - 13518026</p>
      <p>Fikra Hadi Ramadhan - 13518036</p>
      <p>Muhammad Cisco Zulfikar - 13518073</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Result',
  data() {
    return {
      charges: null,
      name: null
    }
  },
  watch:{
    charges(newVal) {
      this.charges = newVal
    },
    name(newVal) {
      this.name = newVal
    }
  },
  mounted() {
    console.log("result", localStorage.getItem("result"));
    console.log("name", localStorage.getItem("nameInsurance"));
    this.name = localStorage.getItem("nameInsurance");
    this.charges = `USD ${parseFloat(localStorage.getItem("result")).toFixed(2)}`;
    // console.log(this.charges)
  },
  methods: {
    back() {
      localStorage.removeItem("result")
      localStorage.removeItem("nameInsurance")
      this.$router.push({ path: "/"})
    }
  }
}
</script>

<style lang="scss" module>
.result__container {
  background: #04AA6D;
  width: 100%;
  height: auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  .content {
    background: #FFFFFF;
    margin: 60px;
    margin-bottom: 20px;
    width: 60%;
    border: none;
    box-shadow: 0 0 25px 0 #008815;
    border-radius: 10px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    .header {
      display: flex;
      justify-content: space-between;
      flex-direction: column;
      align-items: center;
      .title {
        color: #04AA6D;
      }
    }
    .charges {
      display: flex;
      justify-content: space-between;
      flex-direction: column;
      align-items: center;
      width: 90%;
      &__title, &__name {
        font-size: 18px;
        font-weight: bold;
        color: #04AA6D;
        margin-bottom: 0;
      }
      &__title {
        margin-top: 5px;
      }
      div {
        width: 90%;
        display: flex;
        justify-content: space-between;
        flex-direction: row;
        align-items: center;
      }
    }
  }
  .footer {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
    p {
      margin: 0;
      font-size: 12px;
      font-weight: bold;
      color: #FFFFFF;
    }
  }
}
</style>
