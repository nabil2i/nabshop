<template>
  <div class="col">    
    <div class="card">
      <img src="/images/jpg/cdl.jpg" class="card-img-top" alt="">
      <div class="card-body">
        <div><h5 class="card-title"><strong>Chants de lettres</strong></h5></div>
        <div class="card-text">By Nabil Affo</div>
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
</template>

<script>
export default {
  name: 'BookBox',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.btn-nabshop {
  width:150px;
}

.btn-nabshop:hover {
  background-color: rgb(99, 123, 154);
}
</style>
