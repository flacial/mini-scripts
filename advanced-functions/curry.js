const curry = (fn) => {
  const arity = fn.length // fn arguments count
  
  return function $curry(...args) {
    /* 
    bind: create a new function of $curry with "this" (null) referencing the new               function and with all the arguments of $curry.
    */ 
    if (args.length < arity) return $curry.bind(null, ...args)
    
    /*
    call: run the function "fn" with "this" (null) referencing the global scope
    and all the arguments of $curry.
    */
    return fn.call(null, ...args)
  }
}

export default curry
