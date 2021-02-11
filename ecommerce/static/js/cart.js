var updateBtns = document.getElementsByClassName('update-cart');
for (var i=0;i<updateBtns.length;i++)
{
    updateBtns[i].addEventListener("click",function(){
         var productId = this.dataset.product;
         var action = this.dataset.action;
         console.log(productId,action);
         console.log(user);
         if(user=='AnonymousUser')
         {

         }
         else{
             updateitem(productId,action)
         }
    })
    function updateitem(productId,action)
    {
        var url = '/updateitem/'
        fetch(url,{
            method:'POST',
            headers:{
              'Content-Type':'application/json',
              'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'productId':productId,'action':action})
        })
        .then((response)=>{
            return response.json()
        })
        .then((data)=>{
            console.log("data",data)
            location.reload();
        })

    }

}