<template>
  <div :class="$style.home__container">
    <div :class="$style.content">
      <h1 :class="$style.title"></h1>
      <p :class="$style.subtitle"></p>
      <div :class="$style.form">

      </div>
      <button :class="$style.submit"></button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',
}
</script>

<style lang="scss" module>
.home__container {
  background: #202020;
  width: 100%;
  .content {
    width: 70%;
    border: none;
    box-shadow: 0 0 25px 0 #d6e0f5;
    .title {

    }
    .subtitle {

    }
    .form {

    }
    .submit {

    }
  }
}
</style>
