office_list = [{'product':'Stapler','price':'12.19'}, {'product':'Label Maker','price':'35.59'}, {'product':'Printer','price':'119.99'}]

kitchen_list = [{'product':'Knife','price':'14.99'}, {'product':'Cutting Board','price':'13.59'}, {'product':'Toaster','price':'45.99'}]

garage_list = [{'product':'Wrench','price':'9.19'}, {'product':'Paint','price':'23.99'}, {'product':'Vice','price':'89.99'}]

livingroom_list = [{'product':'Lamp','price':'23.50'}, {'product':'Pillow','price':'13.99'}, {'product':'Rug','price':'30.99'}]

patio_list = [{'product':'Fountain','price':'122.19'}, {'product':'Plant','price':'25.99'}, {'product':'Bird Feeder','price':'20.99'}]

document.getElementById('search-form').addEventListener('submit', (event)=>{
    event.preventDefault()

    const searchInput = document.getElementById('product')
    if(searchInput.value === 'Stapler' || searchInput.value === 'stapler'){
        window.location.href = "office"
    }
    else if(searchInput.value === 'Label Maker' || searchInput.value === 'label maker'){
        window.location.href = "office"
    }
    else if(searchInput.value === 'Printer' || searchInput.value === 'printer'){
        window.location.href = "office"
    }
    else if(searchInput.value === 'Knife' || searchInput.value === 'knife'){
        window.location.href = "kitchen"
    }
    else if(searchInput.value === 'Cutting Board' || searchInput.value === 'cutting board'){
        window.location.href = "kitchen"
    }
    else if(searchInput.value === 'Toaster' || searchInput.value === 'toaster'){
        window.location.href = "kitchen"
    }
    else if(searchInput.value === 'Wrench' || searchInput.value === 'wrench'){
        window.location.href = "garage"
    }
    else if(searchInput.value === 'Paint' || searchInput.value === 'paint'){
        window.location.href = "garage"
    }
    else if(searchInput.value === 'Vice' || searchInput.value === 'vice'){
        window.location.href = "garage"
    }
    else if(searchInput.value === 'Lamp' || searchInput.value === 'lamp'){
        window.location.href = "livingroom"
    }
    else if(searchInput.value === 'Pillow' || searchInput.value === 'pillow'){
        window.location.href = "livingroom"
    }
    else if(searchInput.value === 'Rug' || searchInput.value === 'rug'){
        window.location.href = "livingroom"
    }
    else if(searchInput.value === 'Fountain' || searchInput.value === 'fountain'){
        window.location.href = "patio"
    }
    else if(searchInput.value === 'Plant' || searchInput.value === 'plant'){
        window.location.href = "patio"
    }
    else if(searchInput.value === 'Bird Feeder' || searchInput.value === 'bird feeder'){
        window.location.href = "patio"
    }

    else{
        const searchInput = document.getElementById('product')
        document.getElementById('out-of-stock').style.display = "flex"
    
        axios.get('products', {params:{query: searchInput.value}})
        
        .then((response)=>{
            console.log(response.data.url)
            document.getElementById('oos-image').src = response.data.url
        })
    }
})
