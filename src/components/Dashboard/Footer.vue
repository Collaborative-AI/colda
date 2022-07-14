<template>
  <div class="footer dashboard">
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-8 col-12">
          <div class="copyright">
            <p>
              © Copyright {{ new Date().getFullYear() }}
              <a href="https://themeforest.net/user/quixlab/portfolio"
                >Quixlab</a
              >
              I All Rights Reserved
            </p>
          </div>
        </div>
        <div class="col-sm-4 col-12">
          <div class="footer-social">
            <ul>
              <li>
                <a href="#"><i class="fa fa-facebook"></i></a>
              </li>
              <li>
                <a href="#"><i class="fa fa-twitter"></i></a>
              </li>
              <li>
                <a href="#"><i class="fa fa-linkedin"></i></a>
              </li>
              <li>
                <a href="#"><i class="fa fa-youtube"></i></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
};
</script>
