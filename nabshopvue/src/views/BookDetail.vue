<template>
  <div class="home">
    <div class="container mt-5">
      <div class="row">
      
        <div class="col-md-3">
          <img src="/images/jpg/cdl.jpg" class="card-img-top" alt="">
        </div>

        <div class="col-md-6">
          <h5 class=""><strong>Chants de lettres</strong></h5>
          <div class="">By Nabil Affo</div>
          <hr>
          <div class="justify-content-left"> Lorem ipsum dolor sit amet consectetur adipisicing elit. Quae quasi repellat at suscipit amet perspiciatis voluptas aliquid, rerum, animi exercitationem dicta quidem iure minima debitis cupiditate natus velit tenetur saepe tempore? Ipsa soluta non maiores? Impedit hic animi molestias soluta fuga. Necessitatibus culpa animi perspiciatis qui nam, modi expedita natus dolorum assumenda quisquam quae maiores iste sed enim voluptates autem praesentium eligendi a inventore non esse harum soluta reiciendis velit. Temporibus excepturi quasi impedit? Aut, dolore. At optio animi, necessitatibus voluptatum praesentium iste recusandae illum nesciunt aspernatur vel laboriosam voluptatem rem expedita et voluptates nam hic autem magni. Ratione enim fuga est, consectetur illum veritatis expedita voluptas assumenda, ex asperiores reiciendis. Quos aspernatur odit porro explicabo sit quia qui commodi nam iste voluptatibus pariatur quis magnam, eaque soluta voluptate eius molestias! Id, nihil quae. Magnam rem ipsa aspernatur qui, voluptas aperiam tenetur dolorem enim debitis consequuntur quibusdam, beatae ea! Dolorem, totam? Molestias, esse quos dolorem quia placeat aliquid, repellat similique possimus atque, aspernatur minima minus numquam magni reprehenderit ad accusantium aut. Illum nostrum impedit hic laborum incidunt in a amet accusantium voluptatem consequuntur, beatae, corrupti, adipisci obcaecati? Nihil necessitatibus, fugit quia voluptate ipsum molestias dolorum nostrum unde in aut. Suscipit at doloremque odio dolores! Enim ex voluptatibus inventore quibusdam. Ab sunt non consequuntur inventore rerum voluptate veritatis ratione earum modi mollitia perspiciatis, in, nemo atque exercitationem cumque tenetur tempora laborum officiis maiores ad! Eveniet ratione incidunt, veniam perspiciatis delectus optio consequatur doloremque illum ab placeat fuga magni quasi illo? Libero voluptatem impedit laborum quas quis minus ipsum cupiditate tempora. Tempore velit alias dolores at ullam placeat nihil! Architecto pariatur nobis, quibusdam dolorem exercitationem repudiandae fuga magnam doloribus vero nam eveniet reprehenderit fugiat inventore molestias repellendus ex autem dolores. Voluptatum tempora, cumque quasi repudiandae commodi maxime laudantium et rerum accusantium magni.
          </div>
        </div>
      
        <div class="col-md-3 justify-content-left">
          <div><h5 class=""><strong>Details</strong></h5></div>
          <div class=""> <strong> Genre: </strong>Poetry</div>
          <div class=" justify-content-left"><strong>Publication date: </strong> 2022/02/21</div>
          <div class=" justify-content-left"><strong>Format: </strong>A5 (148x120)</div>
          <div class=" justify-content-left"><strong>ISBN: </strong> 15498988997987</div>
          <div class=" justify-content-left"><strong>Pages: </strong> 100</div>
          <div class="mb-2">
            <a href="#" class="btn btn-success btn-nabshop me-2" type="submit"><div>Buy paperback</div>$<span>5.8</span></a>
          </div>
          
          <div>
            <a href="#" class="btn btn-success btn-nabshop" type="submit"><div>Buy Ebook</div>$<span>1.99</span></a>
          </div> 
        </div>

      </div>
    </div>
    <Shopfooter/>
  </div>
</template>

<script>
import Shopfooter from '@/components/Shopfooter.vue'

  export default {
    name: 'Bookdetail',
    components: {
      Shopfooter,
    } 
  }
</script>
 <style scoped>
 .put-left {
  align-items: right;
 }
 </style>