<template>
  <div>
    <div class="qrcode">
      <img src="../../assets/images/qr.svg" alt="" width="150" />
    </div>
    <form action="">
      <div class="input-group">
        <input
          type="text"
          class="form-control"
          value="0xceb1b174085b0058201be4f2cd0da6a21bff85d4"
        />
        <div class="input-group-append">
          <span
            class="input-group-text bg-primary text-white c-pointer"
            @click="doCopy"
            >Copy</span
          >
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "BarCode",
  data() {
    return {
      message: "0xceb1b174085b0058201be4f2cd0da6a21bff85d4",
    };
  },
  methods: {
    doCopy: function() {
      this.$copyText(this.message).then(
        function(e) {
          alert("Copied");
          console.log(e);
        },
        function(e) {
          alert("Can not copy");
          console.log(e);
        }
      );
    },
  },
};
</script>
