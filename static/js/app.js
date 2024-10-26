//  categories slide js  start
// const sliderWrapper = document.querySelector('.slider-wrapper');
// const productCards = document.querySelectorAll('.product-card');
// const prevBtn = document.querySelector('.prev-btn');
// const nextBtn = document.querySelector('.next-btn');
// let currentIndex = 0;
// let slideInterval;

// // Function to slide cards
// function slideTo(index) {
//     const cardWidth = productCards[0].offsetWidth + 16; // Adjust according to product-card css margin 8*2=16 (margin: 0 8px;)
//     const translateXValue = -(index * cardWidth); // Regular translation for full cards
//     sliderWrapper.style.transform = `translateX(${translateXValue}px)`;

//     // Adjust for 30% of the next card on the right
//     if (index < productCards.length - 4) {
//         sliderWrapper.style.transform += `translateX(-${cardWidth * 0.2}px)`;
//     }

//     currentIndex = index;
// }

// // Function to go to the next card
// function nextSlide() {
//     if (currentIndex < productCards.length - 4) {
//         // adjust card qty for each slide 
//         slideTo(currentIndex + 1);
//     } else {
//         slideTo(0);
//     }
// }

// // Function to go to the previous card
// function prevSlide() {
//     if (currentIndex > 0) {
//         // adjust card qty for each slide
//         slideTo(currentIndex - 1);
//     } else {
//         slideTo(productCards.length - 4);
//     }
// }

// // Event Listeners for buttons
// nextBtn.addEventListener('click', nextSlide);
// prevBtn.addEventListener('click', prevSlide);

// // Auto-slide functionality
// function startAutoSlide() {
//     slideInterval = setInterval(nextSlide, 3000); // Adjust interval as needed
// }

// function stopAutoSlide() {
//     clearInterval(slideInterval);
// }

// sliderWrapper.addEventListener('mouseover', stopAutoSlide);
// sliderWrapper.addEventListener('mouseout', startAutoSlide);

// // Initialize the slider
// startAutoSlide();
// slideTo(0); // Start with the first card showing

// categories slide js  end




///////////////////////////////// home page
// product slider js start 
document.querySelectorAll('.slider-wrapper').forEach((sliderWrapper, index) => {
    const productCards = sliderWrapper.querySelectorAll('.product-card');
    const prevBtn = sliderWrapper.closest('.slider-container').querySelector('.prev-btn');
    const nextBtn = sliderWrapper.closest('.slider-container').querySelector('.next-btn');
    let currentIndex = 0;
    let slideInterval;

    function slideTo(index) {
        const cardWidth = productCards[0].offsetWidth + 24; // Adjust according to product-card css margin 8*2=16 (margin: 0 8px;)
        const translateXValue = -(index * cardWidth);
        sliderWrapper.style.transform = `translateX(${translateXValue}px)`;

        if (index < productCards.length - 5) {
            sliderWrapper.style.transform += `translateX(-${cardWidth * 0.4}px)`;
        }

        currentIndex = index;
    }

    function nextSlide() {
        if (currentIndex < productCards.length - 5) {
            slideTo(currentIndex + 1);
        } else {
            slideTo(0);
        }
    }

    function prevSlide() {
        if (currentIndex > 0) {
            slideTo(currentIndex - 1);
        } else {
            slideTo(productCards.length - 5);
        }
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    function startAutoSlide() {
        slideInterval = setInterval(nextSlide, 3000); // Adjust interval as needed
    }

    function stopAutoSlide() {
        clearInterval(slideInterval);
    }

    sliderWrapper.addEventListener('mouseover', stopAutoSlide);
    sliderWrapper.addEventListener('mouseout', startAutoSlide);

    startAutoSlide();
    slideTo(0); // Start with the first card showing
});



// panjabi 3 items slide js start || this problem to cart js
document.querySelectorAll('.slider-3items-wrapper').forEach((sliderWrapper, index) => {
    let productCards = sliderWrapper.querySelectorAll('.product-card');
    const prevBtn = sliderWrapper.closest('.slider-3items-container').querySelector('.prev-btn');
    const nextBtn = sliderWrapper.closest('.slider-3items-container').querySelector('.next-btn');
    let currentIndex = 3; // Start from the first real card set after cloning
    let slideInterval;

    // Clone first and last few slides to create an infinite looping effect
    for (let i = 0; i < 3; i++) {
        const firstClone = productCards[i].cloneNode(true);
        const lastClone = productCards[productCards.length - 1 - i].cloneNode(true);
        sliderWrapper.appendChild(firstClone);
        sliderWrapper.insertBefore(lastClone, sliderWrapper.firstChild);
    }

    // Update productCards to include cloned elements
    productCards = sliderWrapper.querySelectorAll('.product-card');

    // Adjust the initial position to be at the start of the actual cards
    const cardWidth = productCards[0].offsetWidth + 24; // Adjust according to product-card CSS margin
    sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;

    function slideTo(index) {
        const translateXValue = -(index * cardWidth);
        sliderWrapper.style.transition = 'transform 0.5s ease-in-out';
        sliderWrapper.style.transform = `translateX(${translateXValue}px)`;

        currentIndex = index;

        // Handle looping effect
        if (index === 0) {
            setTimeout(() => {
                sliderWrapper.style.transition = 'none';
                currentIndex = productCards.length - 6;
                sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
            }, 500);
        } else if (index === productCards.length - 3) {
            setTimeout(() => {
                sliderWrapper.style.transition = 'none';
                currentIndex = 3;
                sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
            }, 500);
        }
    }

    function nextSlide() {
        slideTo(currentIndex + 1);
    }

    function prevSlide() {
        slideTo(currentIndex - 1);
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    function startAutoSlide() {
        slideInterval = setInterval(nextSlide, 3000); // Adjust interval as needed
    }

    function stopAutoSlide() {
        clearInterval(slideInterval);
    }

    sliderWrapper.addEventListener('mouseover', stopAutoSlide);
    sliderWrapper.addEventListener('mouseout', startAutoSlide);

    startAutoSlide();
});


// six-card slider js start || uses in testimonial-card, categories
document.querySelectorAll('.six-card-slider-wrapper').forEach((sliderWrapper, index) => {
    let productCards = sliderWrapper.querySelectorAll('.six-card');
    const prevBtn = sliderWrapper.closest('.six-card-slider-container').querySelector('.prev-btn');
    const nextBtn = sliderWrapper.closest('.six-card-slider-container').querySelector('.next-btn');
    let currentIndex = 6; // Start from the first real card set after cloning
    let slideInterval;

    // Clone first and last few slides to create infinite looping effect
    for (let i = 0; i < 6; i++) {
        const firstClone = productCards[i].cloneNode(true);
        const lastClone = productCards[productCards.length - 1 - i].cloneNode(true);
        sliderWrapper.appendChild(firstClone);
        sliderWrapper.insertBefore(lastClone, sliderWrapper.firstChild);
    }

    // Update productCards to include cloned elements
    productCards = sliderWrapper.querySelectorAll('.six-card');

    // Adjust the initial position to be at the start of the actual cards
    const cardWidth = productCards[0].offsetWidth + 24; // Adjust according to product-card CSS margin
    sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;

    function slideTo(index) {
        const translateXValue = -(index * cardWidth);
        sliderWrapper.style.transition = 'transform 0.5s ease-in-out';
        sliderWrapper.style.transform = `translateX(${translateXValue}px)`;
        currentIndex = index;

        // Handle looping effect
        if (index === 0) {
            setTimeout(() => {
                sliderWrapper.style.transition = 'none';
                currentIndex = productCards.length - 12;
                sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
            }, 500);
        } else if (index === productCards.length - 6) {
            setTimeout(() => {
                sliderWrapper.style.transition = 'none';
                currentIndex = 6;
                sliderWrapper.style.transform = `translateX(${-cardWidth * currentIndex}px)`;
            }, 500);
        }
    }

    function nextSlide() {
        slideTo(currentIndex + 1);
    }

    function prevSlide() {
        slideTo(currentIndex - 1);
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    function startAutoSlide() {
        slideInterval = setInterval(nextSlide, 3000); // Adjust interval as needed
    }

    function stopAutoSlide() {
        clearInterval(slideInterval);
    }

    sliderWrapper.addEventListener('mouseover', stopAutoSlide);
    sliderWrapper.addEventListener('mouseout', startAutoSlide);

    startAutoSlide();
});



////////////////// store page js start
// <!-- store page filter see more or less js  -->
document.addEventListener('DOMContentLoaded', function() {
document.querySelectorAll('.readmore').forEach(function(link) {
    link.addEventListener('click', function() {
        var currentFilterBox = this.closest('.filter-box');
        document.querySelectorAll('.filter-box.show').forEach(function(fBox) {
            if (fBox !== currentFilterBox) {
                fBox.classList.remove('show');
            }
        });
        currentFilterBox.classList.toggle('show');
    });
});
});


// <!-- store page filter pirce range js start  -->
const rangevalue = document.querySelector(".price-slider-range .price-slider"); 
const rangeInputvalue = document.querySelectorAll(".range-input input"); 

// Set the price gap 
let priceGap = 100; 

// Adding event listners to price input elements 
const priceInputvalue = document.querySelectorAll(".price-input input"); 
for (let i = 0; i < priceInputvalue.length; i++) { 
priceInputvalue[i].addEventListener("input", e => { 

// Parse min and max values of the range input 
let minp = parseInt(priceInputvalue[0].value); 
let maxp = parseInt(priceInputvalue[1].value); 
let diff = maxp - minp 

if (minp < 0) { 
    alert("minimum price cannot be less than 0"); 
    priceInputvalue[0].value = 0; 
    minp = 0; 
} 

// Validate the input values 
if (maxp > 10000) { 
    alert("maximum price cannot be greater than 10000"); 
    priceInputvalue[1].value = 10000; 
    maxp = 10000; 
} 

if (minp > maxp - priceGap) { 
    priceInputvalue[0].value = maxp - priceGap; 
    minp = maxp - priceGap; 

    if (minp < 0) { 
        priceInputvalue[0].value = 0; 
        minp = 0; 
    } 
} 

// Check if the price gap is met 
// and max price is within the range 
if (diff >= priceGap && maxp <= rangeInputvalue[1].max) { 
    if (e.target.className === "min-input") { 
        rangeInputvalue[0].value = minp; 
        let value1 = rangeInputvalue[0].max; 
        rangevalue.style.left = `${(minp / value1) * 100}%`; 
    } 
    else { 
        rangeInputvalue[1].value = maxp; 
        let value2 = rangeInputvalue[1].max; 
        rangevalue.style.right = 
            `${100 - (maxp / value2) * 100}%`; 
        } 
    } 
}); 

// Add event listeners to range input elements 
for (let i = 0; i < rangeInputvalue.length; i++) { 
    rangeInputvalue[i].addEventListener("input", e => { 
        let minVal = 
            parseInt(rangeInputvalue[0].value); 
        let maxVal = 
            parseInt(rangeInputvalue[1].value); 

        let diff = maxVal - minVal 
        
        // Check if the price gap is exceeded 
        if (diff < priceGap) { 
        
            // Check if the input is the min range input 
            if (e.target.className === "min-range") { 
                rangeInputvalue[0].value = maxVal - priceGap; 
            } 
            else { 
                rangeInputvalue[1].value = minVal + priceGap; 
            } 
        } 
        else { 
        
            // Update price inputs and range progress 
            priceInputvalue[0].value = minVal; 
            priceInputvalue[1].value = maxVal; 
            rangevalue.style.left = 
                `${(minVal / rangeInputvalue[0].max) * 100}%`; 
            rangevalue.style.right = 
                `${100 - (maxVal / rangeInputvalue[1].max) * 100}%`; 
            } 
        }); 
    } 
}

// <!-- pirce range js end -->





///////////////////////////////// product details page js start
// product thum img slider js start 
document.querySelectorAll('.thum-slider-wrapper').forEach((sliderWrapper, index) => {
    const productCards = sliderWrapper.querySelectorAll('.product-thum-card');
    const prevBtn = sliderWrapper.closest('.thum-slider-container').querySelector('.prev-btn');
    const nextBtn = sliderWrapper.closest('.thum-slider-container').querySelector('.next-btn');
    let currentIndex = 0;
    let slideInterval;

    function slideTo(index) {
        const cardHeight = productCards[0].offsetHeight + 12; // Adjust according to product-thum-card css margin 8*2=16 (margin: 8px 0;)
        const translateYValue = -(index * cardHeight); // Regular translation for full cards
        sliderWrapper.style.transform = `translateY(${translateYValue}px)`;

        // Adjust for 30% of the next card on the bottom
        if (index < productCards.length - 5) {
            sliderWrapper.style.transform += `translateY(-${cardHeight * 0.2}px)`;
        }

        currentIndex = index;
    }

    function nextSlide() {
        if (currentIndex < productCards.length - 5) {
            slideTo(currentIndex + 1);
        } else {
            slideTo(0);
        }
    }

    function prevSlide() {
        if (currentIndex > 0) {
            slideTo(currentIndex - 1);
        } else {
            slideTo(productCards.length - 5);
        }
    }

    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);

    function startAutoSlide() {
        slideInterval = setInterval(nextSlide, 3000); // Adjust interval as needed
    }

    function stopAutoSlide() {
        clearInterval(slideInterval);
    }

    sliderWrapper.addEventListener('mouseover', stopAutoSlide);
    sliderWrapper.addEventListener('mouseout', startAutoSlide);

    startAutoSlide();
    slideTo(0); // Start with the first card showing
});





// <!-- product view img js start  -->
document.addEventListener('DOMContentLoaded', function () {
// Main product view image
const productViewImg = document.querySelector('.product-view-img');

// Thumbnail images
const thumbImgs = document.querySelectorAll('.product-thum-img');

// Add click event listeners to each thumbnail image
thumbImgs.forEach(function (thumbImg) {
    thumbImg.addEventListener('click', function () {
        // Update the main product view image with the clicked thumbnail's src
        productViewImg.src = this.src;
        });
    });
});




// <!-- color select js start  -->
document.querySelectorAll('.color-img').forEach(function(img) {
img.addEventListener('click', function() {
    // Remove active class from all items
    document.querySelectorAll('.color-item').forEach(function(item) {
        item.classList.remove('active');
    });

    // Add active class to the clicked item
    const parentItem = this.closest('.color-item');
    parentItem.classList.add('active');

    // Update the color name based on the clicked item
    const colorName = parentItem.getAttribute('data-color');
    document.querySelector('.color-name').textContent = colorName;
    });
});



// <!-- size select js start  -->

document.querySelectorAll('.size-item').forEach(function(item) {
item.addEventListener('click', function() {
    // Remove active class from all items
    document.querySelectorAll('.size-item').forEach(function(sizeItem) {
        sizeItem.classList.remove('active');
    });

    // Add active class to the clicked item
    this.classList.add('active');

    // Update the quantity based on the clicked item
    const sizeQty = this.getAttribute('data-qty');
    document.querySelector('.size-qty').textContent = `${sizeQty} available`;
    });
});




// <!-- qty select js start  -->
document.addEventListener('DOMContentLoaded', function () {
const minusBtn = document.querySelector('.qty-minus');
const plusBtn = document.querySelector('.qty-plus');
const qtyInput = document.querySelector('.qty-input');
const availableQty = parseInt(document.querySelector('.available-qty').textContent, 10);

// Minimum quantity allowed
const minQty = 1;

// Decrement quantity
minusBtn.addEventListener('click', function () {
    let currentQty = parseInt(qtyInput.value, 10);
    if (currentQty > minQty) {
        qtyInput.value = currentQty - 1;
    }
});

// Increment quantity
plusBtn.addEventListener('click', function () {
    let currentQty = parseInt(qtyInput.value, 10);
    if (currentQty < availableQty) {
        qtyInput.value = currentQty + 1;
    }
    });
});









// <!-- order cart popup js start -->
let body = document.querySelector("body"); 
let orderCartWrap = document.getElementById('orderCartWrap');

// function showOrderCart(){
//     orderCartWrap.classList.add('overlay')
//     orderCartWrap.delay('800')
//     orderCartWrap.fadeIn('500')
//     body.style.overflow = "hidden"
// }

// function closeOrderCart(){
//     orderCartWrap.classList.remove('overlay')
//     orderCartWrap.delay('800')
//     orderCartWrap.fadeOut('500')
//     body.style.overflow = "auto"
// }

// Helper function to fade in an element
function fadeIn(element, duration = 400) {
    element.style.opacity = 0;
    element.style.display = 'block';

    let last = +new Date();
    const tick = function() {
        element.style.opacity = +element.style.opacity + (new Date() - last) / duration;
        last = +new Date();

        if (+element.style.opacity < 1) {
            (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
        }
    };
    tick();
}

// Helper function to fade out an element
function fadeOut(element, duration = 400) {
    element.style.opacity = 1;

    let last = +new Date();
    const tick = function() {
        element.style.opacity = +element.style.opacity - (new Date() - last) / duration;
        last = +new Date();

        if (+element.style.opacity > 0) {
            (window.requestAnimationFrame && requestAnimationFrame(tick)) || setTimeout(tick, 16);
        } else {
            element.style.display = 'none';
        }
    };
    tick();
}

// Show cart popup
function showOrderCart() {
    orderCartWrap.classList.add('overlay');
    fadeIn(orderCartWrap, 400);
    // body.style.overflow = "hidden";
}

// Hide cart popup
function closeOrderCart() {
    orderCartWrap.classList.remove('overlay');
    fadeOut(orderCartWrap, 400);
    // body.style.overflow = "auto";
}















// order cart qty plus minus js start 
const maxQty = 10;  // Replace this with your actual maximum quantity

// Function to increase quantity
function increaseQty(button) {
    const qtyInput = button.closest('.qty-layout').querySelector('.cart-input');
    let currentValue = parseInt(qtyInput.value);
    if (currentValue < maxQty) {
        qtyInput.value = currentValue + 1;
    }
}

// Function to decrease quantity
function decreaseQty(button) {
    const qtyInput = button.closest('.qty-layout').querySelector('.cart-input');
    let currentValue = parseInt(qtyInput.value);
    if (currentValue > 1) {
        qtyInput.value = currentValue - 1;
    }
}

// Attach event listeners to all cart-plus and cart-minus buttons
document.querySelectorAll('.cart-plus').forEach(button => {
    button.addEventListener('click', function () {
        increaseQty(this);
    });
});

document.querySelectorAll('.cart-minus').forEach(button => {
    button.addEventListener('click', function () {
        decreaseQty(this);
    });
});




// delete items from cart js 
document.querySelectorAll('.btn-delete').forEach(button => {
    button.addEventListener('click', function () {
        // Get the closest 'cart-item' row and remove it
        const cartItem = this.closest('.cart-item');
        if (cartItem) {
            cartItem.remove();
        }
        // Optionally, update the subtotal and gross total after deletion
        updateTotals();
    });
});

// Example function to update subtotal, gross total, etc.
function updateTotals() {
    let subtotal = 0;
    const cartItems = document.querySelectorAll('.cart-item');

    // Loop through all cart items to calculate the subtotal
    cartItems.forEach(item => {
        const priceElement = item.querySelector('.price');
        if (priceElement) {
            const price = parseFloat(priceElement.innerText.replace(/[^\d.-]/g, '')); // Extract price as a number
            subtotal += price;
        }
    });

    // Update the subtotal and gross total in the table
    document.querySelector('td.text-end').innerText = subtotal;
}





////////////////////////////////////////////
// products store page js start 
//  product filter show close js  

document.getElementById('productFilterBtn').addEventListener('click', function() {
    var filterElement = document.querySelector('.product-filter');
    filterElement.style.display = 'block';
});


// Close filter on click of filterCloseBtn
document.getElementById('filterCloseBtn').addEventListener('click', function() {
    var filterElement = document.querySelector('.product-filter');
    filterElement.style.display = 'none';
});
