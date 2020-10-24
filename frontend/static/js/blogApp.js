const copyrightEl = $("#copyright");


function shrinkCopyright(width) {
    if (width.matches) { // If media query matches
        copyrightEl.text = "Copyright © 2020";
    } 
}

// const smWidth = window.matchMedia("(max-width: )")
const mdWidth = window.matchMedia("(max-width: 768px)");
const smWidth = window.matchMedia("(max-width: 576px)");

// shrinkCopyright(mdWidth) // Call listener function at run time
// mdWidth.addListener(shrinkCopyright) // Attach listener function on state changes



