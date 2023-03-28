<template>
  <!-- Footer -->
<footer class="bg-dark text-center text-white mt-5">
  <!-- Grid container -->
  <div class="container p-4">
    <!-- Section: Social media -->
    <section class="mb-4">
      <!-- Facebook -->
      <!-- <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"
        ><i class="fab fa-facebook-f"></i
      ></a> -->

      <!-- Twitter -->
      <a class="btn btn-outline-light btn-floating m-1" href="https://twitter.com/thenabverse" role="button"
        ><i class="fab fa-twitter"></i
      ></a>

      <!-- Google -->
      <!-- <a class="btn btn-outline-light btn-floating m-1" href="#!" role="button"
        ><i class="fab fa-google"></i
      ></a> -->

      <!-- Instagram -->
      <a class="btn btn-outline-light btn-floating m-1" href="https://www.instagram.com/thenabverse/" role="button"
        ><i class="fab fa-instagram"></i
      ></a>

      <!-- Linkedin -->
      <a class="btn btn-outline-light btn-floating m-1" href="https://www.linkedin.com/in/thenabverse/" role="button"
        ><i class="fab fa-linkedin-in"></i
      ></a>

      <!-- Github -->
      <a class="btn btn-outline-light btn-floating m-1" href="https://github.com/nabil2i/" role="button"
        ><i class="fab fa-github"></i
      ></a>
    </section>
    <!-- Section: Social media -->

    <section class="mb-4">
      <p>
        At nabshop experience the power of words!
      </p>
    </section>
    <!-- Section: Links -->
    <section class="">
      <div class="row">
        <div class="col mb-4 mb-md-0">
          <!-- <h5 class="text-uppercase">Links</h5> -->

          <ul class="list-unstyled mb-0">
            <li>
              <router-link to="/conditions" class="text-white">Conditions of Use</router-link>
            </li>
            <li>
              <router-link to="/privacy"  class="text-white">Privacy Policy</router-link>
            </li>
          </ul>
        </div>

        <div class="col-lg-6 col-md-6 mb-4 mb-md-0">
          <!-- <h5 class="text-uppercase">Links</h5> -->

          <ul class="list-unstyled mb-0">
            <li>
              <router-link to="/about"  href="#!" class="text-white">About</router-link>
            </li>
            <li>
              <router-link to="/contact"  class="text-white">Contact</router-link>
            </li>
          </ul>
        </div>
  
      </div>

    </section>
  </div>
  <!-- Grid container -->

  <!-- Copyright -->
  <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
    © 2023 Copyright:
    <a class="text-white" href="#">nabshop.com</a>
  </div>
  <!-- Copyright -->
</footer>
<!-- Footer -->
</template>

<script>
export default {
  name: 'Shopfooter',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
