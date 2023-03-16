<template>
  <div class="container mt-5">
    <h1 class="mt-5 mb-5"> Bookstore</h1>

    <div class="row row-cols-1 row-cols-md-3 g-5">
      <div class="col">
        
        <div class="card">
          <img src="/images/jpg/cdl.jpg" class="card-img-top" alt="">
          <div class="card-body">
            <h5 class="card-title"><strong>Chants de lettres</strong></h5>
            <p class="card-text">By Nabil Affo</p>
        
            <!-- 2 column grid layout -->
            <div class="row mb-4">
              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy paperback -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy paperback</div>$<span>5.8</span></a> 
              </div>

              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy Ebook -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy Ebook</div>$<span>1.99</span></a> 
              </div>
            </div>

          </div>
        </div>
        
      </div>
      

      <div class="col">
        <div class="card">
          <img src="/images/jpg/lv.jpg" class="card-img-top" alt="">
          <div class="card-body">
            <h5 class="card-title"><strong>Le voyage</strong></h5>
            <p class="card-text">By Nabil Affo</p>
        
            <!-- 2 column grid layout -->
            <div class="row mb-4">
              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy paperback -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy paperback</div>$<span>5.8</span></a> 
              </div>

              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy Ebook -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy Ebook</div>$<span>1.99</span></a> 
              </div>
            </div>

          </div>
        </div>
      </div>

      <div class="col">
        <div class="card">
          <img src="/images/jpg/idc.jpg" class="card-img-top" alt="">
          <div class="card-body">
            <h5 class="card-title"><strong>Ivresse de coeur</strong></h5>
            <p class="card-text">By Nabil Affo</p>
        
            <!-- 2 column grid layout -->
            <div class="row mb-4">
              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy paperback -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy paperback</div>$<span>5.8</span></a> 
              </div>

              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy Ebook -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy Ebook</div>$<span>1.99</span></a> 
              </div>
            </div>

          </div>
        </div>
      </div>

      <div class="col">
        <div class="card">
          <img src="/images/jpg/s.jpg" class="card-img-top" alt="">
          <div class="card-body">
            <h5 class="card-title"><strong>Serenata</strong></h5>
            <p class="card-text">By Nabil Affo</p>
        
            <!-- 2 column grid layout -->
            <div class="row mb-4">
              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy paperback -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy paperback</div>$<span>5.8</span></a> 
              </div>

              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy Ebook -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy Ebook</div>$<span>1.99</span></a> 
              </div>
            </div>

          </div>
        </div>
      </div>

      <div class="col">
        <div class="card">
          <img src="/images/jpg/es.jpg" class="card-img-top" alt="">
          <div class="card-body">
            <h5 class="card-title"><strong>Eastern Storms</strong></h5>
            <p class="card-text">By Nabil Affo</p>
        
            <!-- 2 column grid layout -->
            <div class="row mb-4">
              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy paperback -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy paperback</div>$<span>5.8</span></a> 
              </div>

              <div class="col-md-6 d-flex justify-content-center">
                <!-- Buy Ebook -->
                <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy Ebook</div>$<span>1.99</span></a> 
              </div>
            </div>

          </div>
        </div>
      </div>

    </div>
  </div>  
</template>

<script>
export default {
  name: 'Store',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.loginform {

  width: 400px;
  height: min-content;
  border: 2px;
  border-radius: 7px;
  background: rgb(219, 217, 217);
  padding: 20px 40px;
  margin-top: 50px
}

.btn-nabshop {
  width:150px;
}

.btn-nabshop:hover {
  background-color: rgb(99, 123, 154);
}

</style>
