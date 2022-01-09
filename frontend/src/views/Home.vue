<template>
  <div :class="$style.home__container">
    <div :class="$style.content">
      <div :class="$style.header">
        <h1 :class="$style.title">Prediksi Biaya Asuransi Kesehatan</h1>
        <p :class="$style.subtitle">
          Memprediksi biaya yang harus dibayarkan untuk asuransi kesehatan
        </p>
      </div>
      <div :class="$style.form">
        <p :class="$style.form__title">Silahkan Isi Data Berikut</p>
        <form 
          @submit="submitForm"
          action=""
          method="post"
        >
          <p>
            <label for="name">Nama</label><br>
            <input 
              id="name"
              type="text" 
              name="name" 
              v-model="forms.name"
              :class="[$style.items, $style.name]"
            >
          </p>
          <p>
            <label for="age">Umur</label><br>
            <select
              id="age" 
              name="age" 
              v-model="forms.age"
              :class="[$style.items, $style.age]"
            >
              <option 
                v-for="el in 101"
                :key="el"
                :value="el-1"
              >
                {{ el-1 }}
              </option>
            </select>
          </p>
          <p>
            <label for="sex">Jenis Kelamin</label><br>
            <select
              id="sex"
              name="sex" 
              v-model="forms.sex"
              :class="[$style.items, $style.sex]"
            >
              <option :value="0">Perempuan</option>
              <option :value="1">Laki-Laki</option>
            </select>
          </p>
          <p>
            <label for="weight">Berat Badan (Dalam kg)</label><br>
            <input
              id="weight"
              name="weight" 
              type="number"
              min="0"
              v-model="forms.weight"
              :class="[$style.items, $style.weight]"
            >
          </p>
          <p>
            <label for="height">Tinggi Badan (Dalam cm)</label><br>
            <input
              id="height"
              name="height" 
              type="number"
              min="0"
              v-model="forms.height"
              :class="[$style.items, $style.height]"
            >
          </p>
          <p>
            <label for="children">Jumlah Anak</label><br>
            <select
              id="children" 
              name="children" 
              v-model="forms.children"
              :class="[$style.items, $style.children]"
            >
              <option 
                v-for="el in 6"
                :key="el"
                :value="el-1"
              >
                {{ el-1 }}
              </option>
            </select>
          </p>
          <p>
            <label for="smoker">Apakah kamu perokok?</label><br>
            <select
              id="smoker" 
              name="smoker" 
              v-model="forms.smoker"
              :class="[$style.items, $style.smoker]"
            >
              <option :value="0">Tidak</option>
              <option :value="1">Iya</option>
            </select>
          </p>
          <p>
            <label for="region">Asal Daerah</label><br>
            <select
              id="region" 
              name="region" 
              v-model="forms.region"
              :class="[$style.items, $style.region]"
            >
              <option :value="0">Sumatra dan Sekitarnya</option>
              <option :value="1">Kalimantan dan Sekitarnya</option>
              <option :value="2">Jawa, Bali, dan Sekitarnya</option>
              <option :value="3">Sulawesi, Papua, dan Sekitarnya</option>
            </select>
          </p>
          <p :class="$style.button">
            <button :class="$style.submit" @click="submitForm">Kirim</button>
          </p>
        </form>
      </div>
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
import axios from 'axios';

export default {
  name: 'Home',
  data() {
    return {
      forms: {
        name: null,
        age: null,
        sex: null,
        height: null,
        weight: null,
        bmi: null,
        children: null,
        smoker: null,
        region: null,
        charges: null,
      }
    }
  },
  methods: {
    async postForm() {
      await axios({
        method: 'POST',
        url: 'https://post-api-insurance.herokuapp.com/postAPI',
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Content-Type': 'application/json',
        },
        data: {
          val: {
            age: this.forms.age,
            sex: this.forms.sex,
            bmi: this.forms.bmi,
            children: this.forms.children,
            smoker: this.forms.smoker,
            region: this.forms.region,
          }
        }
      }).then(response => localStorage.setItem("result", response.data))
      localStorage.setItem('nameInsurance', this.forms.name)
    },
    bmi() {
      this.forms.bmi = this.forms.weight/(Math.pow(this.forms.height/100,2))
    },
    async submitForm() {
      this.bmi()
      await this.postForm()
      this.openResult()
    },
    openResult() {
      this.$router.push({ path: "/result" })
    }
  }
}
</script>

<style lang="scss" module>
.home__container {
  background: #04AA6D;
  width: 100%;
  height: 100%;
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
    .form {
      display: flex;
      justify-content: space-between;
      flex-direction: column;
      align-items: center;
      width: 80%;
      &__title {
        font-size: 18px;
        font-weight: bold;
        color: #04AA6D;
      }
      form {
        display: flex;
        justify-content: space-between;
        flex-direction: column;
        align-items: flex-start;
        width: 100%;
        p {
          margin: 5px;
          width: 100%;
          label {
            font-size: 14px;
          }
          input {
            width: 650px;
            padding: 2px;
          }
          select {
            width: 658px;
            padding: 3px;
            cursor: pointer;
            option:hover {
              cursor: pointer;
            }
          }
          &.button {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            margin-top: 20px;
          }
          .submit {
            background: #04AA6D;
            color: #FFFFFF;
            border: none;
            border-radius: 5px;
            padding: 5px 50px;
            font-size: 16px;
            cursor: pointer;
          }
        }
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
