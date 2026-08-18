---
permalink: "devmtg/2013-11/slides/Fischer-Julia.html"
---
talk2 slides <!-- General and theme style sheets -->   <!-- For syntax highlighting -->  <!-- If the query includes 'print-pdf', use the PDF print sheet --> <!--[if lt IE 9]> <script src="reveal.js/lib/js/html5shiv.js"></script> <![endif]--> <!-- Custom stylesheet, it must be in the same directory as the html file --> 

# Julia: An LLVM-based approach to scientific computing[¶](#Julia:-An-LLVM-based-approach-to-scientific-computing)

Keno Fischer

In \[1\]:

```
run(`git config --get user.name`)
```

```
Keno Fischer
```

# Agenda[¶](#Agenda)

*   Julia, the language
*   A Journey through the CodeGen

# Is it any fast?[¶](#Is-it-any-fast?)

<div style="display: none">

In \[2\]:

```
using Gadfly
using WWWClient
using DataFrames
const w = WWWClient
```

```
Warning: New definition 
    round(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    round(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    round(DataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    round(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    round(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    round(DataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    round(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    round(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    round(AbstractDataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    round(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    round(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    round(AbstractDataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    ceil(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    ceil(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    ceil(DataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    ceil(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    ceil(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    ceil(DataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    ceil(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    ceil(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    ceil(AbstractDataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    ceil(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    ceil(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    ceil(AbstractDataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    floor(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    floor(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    floor(DataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    floor(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    floor(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    floor(DataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    floor(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    floor(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    floor(AbstractDataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    floor(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    floor(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    floor(AbstractDataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    trunc(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    trunc(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    trunc(DataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    trunc(DataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:350
is ambiguous with: 
    trunc(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    trunc(DataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    trunc(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    trunc(AbstractArray{T<:Real,1},) at operators.jl:236.
To fix, define 
    trunc(AbstractDataArray{_<:Real,1},)
before the new definition.
Warning: New definition 
    trunc(AbstractDataArray{T<:Number,N},Integer...) at /Users/kfischer/.julia/DataFrames/src/operators.jl:359
is ambiguous with: 
    trunc(AbstractArray{T<:Real,2},) at operators.jl:237.
To fix, define 
    trunc(AbstractDataArray{_<:Real,2},)
before the new definition.
Warning: New definition 
    formatter(
```

```
Array{T,N},Date{C<:Calendar}...)
is ambiguous with: 
    formatter(Array{T,N},FloatingPoint...).
To fix, define 
    formatter(Array{T,N},)
before the new definition.
Warning: New definition 
    |(SynchronousStepCollection,Any) at /Users/kfischer/.julia/BinDeps/src/BinDeps.jl:283
is ambiguous with: 
    |(Any,NAtype) at /Users/kfischer/.julia/DataFrames/src/operators.jl:385.
To fix, define 
    |(SynchronousStepCollection,NAtype)
before the new definition.
Warning: New definition 
    |(Any,SynchronousStepCollection) at /Users/kfischer/.julia/BinDeps/src/BinDeps.jl:286
is ambiguous with: 
    |(NAtype,Any) at /Users/kfischer/.julia/DataFrames/src/operators.jl:385.
To fix, define 
    |(NAtype,SynchronousStepCollection)
before the new definition.
WARNING: BinDeps.find_library is deprecated, use Base.find_library instead.
WARNING: add_library_mapping is deprecated, use push!(DL_LOAD_PATH,"/path/to/search") instead.
Warning: New definition 
    +(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N}) at operators.jl:253
is ambiguous with: 
    +(DataArray{T,N},AbstractArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:201.
To fix, define 
    +(DataArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N})
before the new definition.
Warning: New definition 
    +(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N}) at operators.jl:253
is ambiguous with: 
    +(AbstractDataArray{T,N},AbstractArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:220.
To fix, define 
    +(AbstractDataArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N})
before the new definition.
Warning: New definition 
    +(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N}) at operators.jl:253
is ambiguous with: 
    +(AbstractArray{T,N},DataArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:201.
To fix, define 
    +(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},DataArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N})
before the new definition.
Warning: New definition 
    +(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N}) at operators.jl:253
is ambiguous with: 
    +(AbstractArray{T,N},AbstractDataArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:220.
To fix, define 
    +(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractDataArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N})
before the new definition.
Warning: New definition 
    -(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N}) at operators.jl:253
is ambiguous with: 
    -(DataArray{T,N},AbstractArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:201.
To fix, define 
    -(DataArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N})
before the new definition.
Warning: New definition 
    -(AbstractArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N}) at operators.jl:253
is ambiguous with: 
    -(AbstractDataArray{T,N},AbstractArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:220.
To fix, define 
    -(AbstractDataArray{T1<:Union(AbstractCalendarDuration,CalendarTime),N},AbstractArray{T2<:Union(AbstractCalendarDuration,CalendarTime),N})
before the new definition.
Warning: New definition 
    *(Any,AbstractCalendarDuration) at /Users/kfischer/.julia/Calendar/src/Calendar.jl:341
is ambiguous with: 
    *(MeasureNil,Any) at /Users/kfischer/.julia/Compose/src/measure.jl:32.
To fix, define 
    *(MeasureNil,AbstractCalendarDuration)
before the new definition.
Warning: New definition 
    -(AbstractArray{T1<:CalendarTime,N},AbstractArray{T2<:CalendarTime,N}) at operators.jl:253
is ambiguous with: 
    -(DataArray{T,N},AbstractArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:201.
To fix, define 
    -(DataArray{T1<:CalendarTime,N},AbstractArray{T2<:CalendarTime,N})
before the new definition.
Warning: New definition 
    -(AbstractArray{T1<:CalendarTime,N},AbstractArray{T2<:CalendarTime,N}) at operators.jl:253
is ambiguous with: 
    -(AbstractDataArray{T,N},AbstractArray{T,N}) at /Users/kfischer/.julia/DataFrames/src/operators.jl:220.
To fix, define 
    -(AbstractDataArray{T1<:CalendarTime,N},AbstractArray{T2<:CalendarTime,N})
before the new definition.
```

Out\[2\]:

```
WWWClient
```

</div>

<div style="display: none">

In \[3\]:

```
function DataFrames.to_io(x::URI) 
    x = IOBuffer(WWWClient.get(x).data)
    x,nb_available(x)
end
```

Out\[3\]:

```
to_io (generic function with 2 methods)
```

</div>

In \[3\]:

```
benchmarks = readtable(URI("http://julialang.org/benchmarks.csv");header=false,colnames=["Language","Benchmark","Time"])
benchmarks = join(benchmarks, subset(benchmarks, :(Language .== "c")),
                  on="Benchmark", kind=:outer)
within!(benchmarks, :(Time ./= Time_1));
```

<div style="display: none">

In \[3\]:

```
# Some cosmetic adjustments. Not essential to the plot, so let's skip them for the sake of space
# Reorder factors
benchmarks["Language"] = PooledDataArray(benchmarks["Language"])
benchmarks["Language"] = reorder(benchmarks["Language"], benchmarks["Time"])
benchmarks["Benchmark"] = PooledDataArray(benchmarks["Benchmark"])
benchmarks["Benchmark"] = reorder(benchmarks["Benchmark"], benchmarks["Time"])

# Capitalize
capitalize(str) = string(uppercase(str[1]) , str[2:end])
benchmarks["Language"] = set_levels(benchmarks["Language"],
                                     Dict{Any, Any}(benchmarks["Language"],
                                          [capitalize(l)
                                           for l in benchmarks["Language"]]))

benchmarks = subset(benchmarks, :(Language .!= "C"))

set_default_plot_size(8inch,8inch/golden);
```

</div>

In \[4\]:

```
p = plot(benchmarks, x="Language", y="Time", color="Benchmark", Scale.y_log10,
     Guide.ylabel("time relative to C"), Guide.xlabel("smaller is better"))
```

Out\[4\]:

Sure, but that's not the main point. So what is? What is different about Julia?

## Dynamic Multiple Dispatch Everywhere[¶](#Dynamic-Multiple-Dispatch-Everywhere)

In \[5\]:

```
convert
```

Out\[5\]:

```
convert (generic function with 464 methods)
```

In \[6\]:

```
+
```

Out\[6\]:

```
+ (generic function with 188 methods)
```

In \[7\]:

```
@which convert(Float64,1)
@which 1.0 + 2
```

```
convert(::Type{Float64},x::Int64) at float.jl:21
+(x::Number,y::Number) at promotion.jl:148
```

## Basic Dispatch[¶](#Basic-Dispatch)

In \[8\]:

```
f(a::Any, b) = "fallback"
f(a::Number, b::Number) = "a and b are both numbers"
f(a::Number, b) = "a is a number"
f(a, b::Number) = "b is a number"
f(a::Integer, b::Integer) = "a and b are both integers"
```

Out\[8\]:

```
f (generic function with 5 methods)
```

In \[9\]:

```
f(1.5,2)
```

Out\[9\]:

```
"a and b are both numbers"
```

In \[10\]:

```
f(1,"bar")
```

Out\[10\]:

```
"a is a number"
```

In \[11\]:

```
f(1,2)
```

Out\[11\]:

```
"a and b are both integers"
```

In \[12\]:

```
f("foo",[1,2])
```

Out\[12\]:

```
"fallback"
```

In \[13\]:

```
methods(f)
```

Out\[13\]:

```
# 5 methods for generic function "f":
f(a::Integer,b::Integer) at In[8]:5
f(a::Number,b::Number) at In[8]:2
f(a::Number,b) at In[8]:3
f(a,b::Number) at In[8]:4
f(a,b) at In[8]:1
```

### Diagonal Dispatch/Parametric Dispatch[¶](#Diagonal-Dispatch/Parametric-Dispatch)

In \[14\]:

```
f{T<:Number}(a::T, b::T) = "a and b are both $(T)s"
f{T<:Number}(a::Vector{T}, b::Vector{T}) = "a and b are both vectors of $(T)s"
```

Out\[14\]:

```
f (generic function with 7 methods)
```

In \[15\]:

```
f(big(1.5),big(1.0)) #Two BigFloats
f([1.0,2.0],[3.0,4.0]) #Two Array{Float64,1}
f([1,2],[3.,4]) #One Array{Int64,1} & One Array{Float64,1}
```

Out\[15\]:

```
"fallback"
```

In \[16\]:

```
f(1,2) #Still more specific
```

Out\[16\]:

```
"a and b are both integers"
```

### That's nice, but what does this have to do with speed?[¶](#That's-nice,-but-what-does-this-have-to-do-with-speed?)

In \[17\]:

```
import Base.LinAlg.det
function det{T}(A::AbstractArray{T,2}) 
    n = size(A)[1]
    n == size(A)[2] || error("Only square matrices allowed")
    n == 2 && return A[1,1]*A[2,2] - A[1,2]*A[2,1]
    s = zero(T)
    for i = 1:n
        s += (-one(T))^(i-1)*A[1,i]*(det(hcat(A[2:end,1:(i-1)],A[2:end,(i+1):end])))
    end
    s
end
```

Out\[17\]:

```
det (generic function with 17 methods)
```

In \[18\]:

```
methods(det)
```

Out\[18\]:

```
# 17 methods for generic function "det":
det(A::Triangular{T<:Number}) at linalg/triangular.jl:63
det(W::Woodbury{T}) at linalg/woodbury.jl:84
det(A::Tridiagonal{T}) at linalg/tridiag.jl:357
det(D::Diagonal{T}) at linalg/diagonal.jl:80
det{T<:Union(Float32,Complex{Float64},Complex{Float32},Float64)}(A::AbstractArray{T<:Union(Float32,Complex{Float64},Complex{Float32},Float64),2}) at linalg/dense.jl:416
det(x::Number) at linalg/dense.jl:419
det{T}(C::Cholesky{T}) at linalg/factorization.jl:44
det{T}(C::CholeskyPivoted{T}) at linalg/factorization.jl:122
det{T}(A::LU{T}) at linalg/factorization.jl:186
det(A::Eigen{T,V}) at linalg/factorization.jl:533
det{T}(lu::LUTridiagonal{T}) at linalg/tridiag.jl:353
det{Tv<:Float64,Ti<:Int32}(lu::UmfpackLU{Tv<:Float64,Ti<:Int32}) at linalg/umfpack.jl:189
det{Tv<:Complex{Float64},Ti<:Int32}(lu::UmfpackLU{Tv<:Complex{Float64},Ti<:Int32}) at linalg/umfpack.jl:197
det{Tv<:Float64,Ti<:Int64}(lu::UmfpackLU{Tv<:Float64,Ti<:Int64}) at linalg/umfpack.jl:189
det{Tv<:Complex{Float64},Ti<:Int64}(lu::UmfpackLU{Tv<:Complex{Float64},Ti<:Int64}) at linalg/umfpack.jl:197
det(L::CholmodFactor{Tv<:Union(Float32,Complex{Float64},Complex{Float32},Float64),Ti<:Union(Int64,Int32)}) at linalg/cholmod.jl:1039
det{T}(A::AbstractArray{T,2}) at In[17]:3
```

### But what about numbers??[¶](#But-what-about-numbers??)

In \[19\]:

```
# This code is taken 1:1 from boot.jl
baremodule FakeMain
abstract Number
abstract Real     <: Number
abstract FloatingPoint <: Real
abstract Integer  <: Real
abstract Signed   <: Integer
abstract Unsigned <: Integer

bitstype 16 Float16 <: FloatingPoint
bitstype 32 Float32 <: FloatingPoint
bitstype 64 Float64 <: FloatingPoint

bitstype 8  Bool <: Integer
bitstype 32 Char <: Integer

bitstype 8   Int8    <: Signed
bitstype 8   Uint8   <: Unsigned
bitstype 16  Int16   <: Signed
bitstype 16  Uint16  <: Unsigned
bitstype 32  Int32   <: Signed
bitstype 32  Uint32  <: Unsigned
bitstype 64  Int64   <: Signed
bitstype 64  Uint64  <: Unsigned
bitstype 128 Int128  <: Signed
bitstype 128 Uint128 <: Unsigned
end
```

### The promotion system[¶](#The-promotion-system)

In \[20\]:

```
+(x::Number, y::Number) = +(promote(x,y)...)
*(x::Number, y::Number) = *(promote(x,y)...)
-(x::Number, y::Number) = -(promote(x,y)...)
/(x::Number, y::Number) = /(promote(x,y)...)
```

```
Warning: Method definition +(Number,Number) in module Base at promotion.jl:148 overwritten in module Main at In[20]:1.
Warning: Method definition *(Number,Number) in module Base at promotion.jl:149 overwritten in module Main at In[20]:2.
Warning: Method definition -(Number,Number) in module Base at promotion.jl:150 overwritten in module Main at In[20]:3.
Warning: Method definition /(Number,Number)
```

Out\[20\]:

```
/ (generic function with 79 methods)
```

In \[21\]:

```
baremodule FakeBase

promote_type{T,S}(::Type{T}, ::Type{S}) =
    promote_result(T, S, promote_rule(T,S), promote_rule(S,T))

promote_rule(T, S) = None

promote_result(t,s,T,S) = typejoin(T,S)
# If no promote_rule is defined, both directions give None. In that
# case use typejoin on the original types instead.
promote_result{T,S}(::Type{T},::Type{S},::Type{None},::Type{None}) = typejoin(T, S)

end
```

### Example: Modular Integers[¶](#Example:-Modular-Integers)

In \[22\]:

```
module ModInts
export ModInt
import Base: -, +, *, convert, promote_rule, show, showcompact

immutable ModInt{n} <: Integer
    k::Int
    ModInt(k) = new(k % n)
end

-{n}(a::ModInt{n}) = ModInt{n}(-a.k)
+{n}(a::ModInt{n}, b::ModInt{n}) = ModInt{n}(a.k+b.k)
-{n}(a::ModInt{n}, b::ModInt{n}) = ModInt{n}(a.k-b.k)
*{n}(a::ModInt{n}, b::ModInt{n}) = ModInt{n}(a.k*b.k)

convert{n}(::Type{ModInt{n}}, i::Int) = ModInt{n}(i)
promote_rule{n}(::Type{ModInt{n}}, ::Type{Int}) = ModInt{n}

show{n}(io::IO, k::ModInt{n}) = print(io, "$(k.k) mod $n")
showcompact(io::IO, k::ModInt) = print(io, k.k)

end # module

using ModInts
```

In \[23\]:

```
a = ModInt{11}(11119)
```

Out\[23\]:

```
9 mod 11
```

In \[24\]:

```
b = ModInt{11}(12345)
```

Out\[24\]:

```
3 mod 11
```

In \[25\]:

```
a+b
```

Out\[25\]:

```
1 mod 11
```

In \[26\]:

```
a*b
```

Out\[26\]:

```
5 mod 11
```

In \[27\]:

```
n = 8
A = map(ModInt{11}, rand(1:100,n,n))
```

Out\[27\]:

```
8x8 Array{ModInt{11},2}:
 10  1   1   3   1  9   7   0
  2  4   9   3   4  3  10   4
  4  0   0   0  10  1  10   1
 10  9   5   7   2  5   7   0
  6  2  10   0   9  4  10   4
  0  9   6   2   3  4   1   2
  8  6  10  10   1  7   4   5
  9  0   7   1   5  4   1  10
```

In \[28\]:

```
A^2 + A + 4
```

Out\[28\]:

```
8x8 Array{ModInt{11},2}:
  3  6   8   6   1   2  4   0
  9  5  10   2  10  10  2   2
 10  9   1   9   5   5  8   8
  4  4   2  10   2   1  4  10
  9  2   5   8   8   7  6   6
  0  5   3   1   3   6  0   5
  8  1   0   9   7  10  2  10
  5  8   3   1   0   8  4   0
```

### Cailey-Hamilton[¶](#Cailey-Hamilton)

Theorem: Every Matrix satisfies its own characteristic polynomial.

Let's Check

<div style="display: none">

In \[29\]:

```
using Polynomial
```

```
in module Base at promotion.jl:151 overwritten in module Main at In[20]:4.
Warning: New definition 
    promote_rule(Type{Poly{T}},Type{T}) at /Users/kfischer/.julia/Polynomial/src/Polynomial.jl:19
is ambiguous with: 
    promote_rule(Type{T},Type{NAtype}) at /Users/kfischer/.julia/DataFrames/src/natype.jl:32.
To fix, define 
    promote_rule(Type{Poly{T}},Type{NAtype})
```

</div>

In \[30\]:

```
using Polynomial
λ = Poly(ModInt{11}[0,1])
p=det(A-map(x->λ*x,eye(ModInt{11},n,n)))
```

Out\[30\]:

```
Poly(-7 mod 11 + 10 mod 11x^2 + -1 mod 11x^3 + -7 mod 11x^4 + 9 mod 11x^5 + -8 mod 11x^6 + -4 mod 11x^7 + x^8)
```

In \[31\]:

```
papply(p,A)
```

Out\[31\]:

```
8x8 Array{ModInt{11},2}:
 0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0
 0  0  0  0  0  0  0  0
```

### Or with Smileys[¶](#Or-with-Smileys)

In \[32\]:

```
import Base: promote_rule, convert, show, one, zero
immutable Face <: Number
  v::Bool
end
+(x::Face,y::Face) = Face(x.v$y.v)
*(x::Face,y::Face) = Face(x.v&y.v)
-(x::Face,y::Face) = x+y
-(x::Face) = x
one(::Type{Face}) = ☺
zero(::Type{Face}) = ☹
Base.show(io::IO,f::Face) = print(io,f.v?'☺':'☹')
Base.convert(::Type{Face},x) = Face(convert(Bool,x))
Base.convert(::Type{Bool},x::Face) = x.v
const ☺ = Face(true)
const ☹ = Face(false)
```

Out\[32\]:

```
☹
```

In \[33\]:

```
n=8
A=map(Face,randbool(n,n))
```

Out\[33\]:

```
8x8 Array{Face,2}:
 ☹  ☹  ☹  ☹  ☹  ☺  ☹  ☹
 ☺  ☺  ☹  ☹  ☹  ☺  ☺  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☺  ☹  ☹  ☹  ☺  ☺  ☹  ☺
 ☹  ☹  ☺  ☺  ☹  ☹  ☹  ☺
 ☺  ☺  ☺  ☺  ☺  ☹  ☹  ☺
 ☹  ☺  ☹  ☺  ☹  ☹  ☺  ☺
 ☺  ☺  ☺  ☹  ☹  ☹  ☹  ☺
```

In \[34\]:

```
using Polynomial
λ = Poly([☹,☺])
λI = map(x->λ*x,eye(Face,n,n))
p=det(A-λI)
```

Out\[34\]:

```
Poly(x^3 + x^5 + x^7 + x^8)
```

In \[35\]:

```
papply(p,A)
```

Out\[35\]:

```
8x8 Array{Face,2}:
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
 ☹  ☹  ☹  ☹  ☹  ☹  ☹  ☹
```

# How does it work?[¶](#How-does-it-work?)

In \[36\]:

```
a = ModInt{11}(11119)
```

Out\[36\]:

```
9 mod 11
```

In \[37\]:

```
b = ModInt{11}(12345)
```

Out\[37\]:

```
3 mod 11
```

In \[38\]:

```
a+b
```

Out\[38\]:

```
1 mod 11
```

In \[39\]:

```
code_llvm(+,(ModInt{11},ModInt{11}))
```

```
before the new definition.
```

```
; Function Attrs: sspreq
define %ModInt @"julia_+6067"(%ModInt, %ModInt) #2 {
top:
  %2 = extractvalue %ModInt %0, 0, !dbg !27934
  %3 = extractvalue %ModInt %1, 0, !dbg !27934
  %4 = add i64 %3, %2, !dbg !27934
  %5 = srem i64 %4, 11, !dbg !27934
  %6 = insertvalue %ModInt undef, i64 %5, 0, !dbg !27934, !julia_type !27939
  ret %ModInt %6, !dbg !27934
}
```

In \[40\]:

```
code_native(+, (ModInt{11},ModInt{11}))
```

```
.section	__TEXT,__text,regular,pure_instructions
Filename: In[22]
Source line: 11
	push	rbp
	mov	rbp, rsp
	sub	rsp, 16
	mov	rcx, rdi
Source line: 11
	movabs	rdi, 4348774360
	mov	rax, qword ptr [rdi]
	mov	qword ptr [rbp - 8], rax
	add	rcx, rsi
	movabs	rdx, 3353953467947191203
	mov	rax, rcx
	imul	rdx
	mov	rax, qword ptr [rdi]
	cmp	rax, qword ptr [rbp - 8]
	jne	29
	mov	rax, rdx
	shr	rax, 63
	sar	rdx
	add	rdx, rax
	imul	rax, rdx, 11
	sub	rcx, rax
	mov	rax, rcx
	add	rsp, 16
	pop	rbp
	ret
	movabs	rax, 140735631254601
	call	rax
```

### Parsing[¶](#Parsing)

In \[41\]:

```
poly = :(A^3+2A-1)
```

Out\[41\]:

```
:(-(+(^(A,3),*(2,A)),1))
```

In \[42\]:

```
ex = :(evaluate_a_polynomial(A) = $poly)
```

Out\[42\]:

```
:(evaluate_a_polynomial(A) = -(+(^(A,3),*(2,A)),1))
```

In \[43\]:

```
dump(ex)
```

```
Expr 
  head: Symbol =
  args: Array(Any,(2,))
    1: Expr 
      head: Symbol call
      args: Array(Any,(2,))
        1: Symbol evaluate_a_polynomial
        2: Symbol A
      typ: Any
    2: Expr 
      head: Symbol call
      args: Array(Any,(3,))
        1: Symbol -
        2: Expr 
          head: Symbol call
          args: Array(Any,(3,))
          typ: Any
        3: Int64 1
      typ: Any
  typ: Any
```

In \[44\]:

```
eval(ex)
```

Out\[44\]:

```
evaluate_a_polynomial (generic function with 1 method)
```

In \[45\]:

```
evaluate_a_polynomial |> methods
```

Out\[45\]:

```
# 1 method for generic function "evaluate_a_polynomial":
evaluate_a_polynomial(A)
```

In \[46\]:

```
typeof(A)
```

Out\[46\]:

```
Array{Face,2}
```

In \[47\]:

```
typeof(a)
```

Out\[47\]:

```
ModInt{11} (constructor with 1 method)
```

In \[48\]:

```
code_lowered(evaluate_a_polynomial,(typeof(A),))
```

Out\[48\]:

```
1-element Array{Any,1}:
 :($(Expr(:lambda, {:A}, {{},{{:A,:Any,0}},{}}, quote 
        return -(+(^(A,3),*(2,A)),1)
    end)))
```

In \[49\]:

```
code_lowered(evaluate_a_polynomial,(typeof(a),))
```

Out\[49\]:

```
1-element Array{Any,1}:
 :($(Expr(:lambda, {:A}, {{},{{:A,:Any,0}},{}}, quote 
        return -(+(^(A,3),*(2,A)),1)
    end)))
```

## So if there's no difference, why pass in the type?[¶](#So-if-there's-no-difference,-why-pass-in-the-type?)

In \[50\]:

```
evaluate_a_polynomial(x::typeof(a)) = 14x^6+3x^2+2x+3
```

Out\[50\]:

```
evaluate_a_polynomial (generic function with 2 methods)
```

In \[51\]:

```
code_lowered(evaluate_a_polynomial,(typeof(a),))
```

Out\[51\]:

```
1-element Array{Any,1}:
 :($(Expr(:lambda, {:x}, {{},{{:x,:Any,0}},{}}, quote  # In[50], line 1:
        return +(*(14,^(x,6)),*(3,^(x,2)),*(2,x),3)
    end)))
```

In \[52\]:

```
function a_more_complicated_function(A)
    if sum(sum(A)) > 0
        return :ok
    else 
        return 0
    end
end
```

Out\[52\]:

```
a_more_complicated_function (generic function with 1 method)
```

In \[53\]:

```
code_lowered(a_more_complicated_function,(typeof(A),))
```

Out\[53\]:

```
1-element Array{Any,1}:
 :($(Expr(:lambda, {:A}, {{},{{:A,:Any,0}},{}}, quote  # In[52], line 2:
        unless >(sum(sum(A)),0) goto 0 # line 3:
        return :ok
        goto 1
        0:  # In[52], line 5:
        return 0
        1: 
    end)))
```

# Type inference[¶](#Type-inference)

In \[54\]:

```
code_typed(evaluate_a_polynomial,(typeof(A),))
```

Out\[54\]:

```
1-element Array{Any,1}:
 :($(Expr(:lambda, {:A}, {{},{{:A,Array{Face,2},0}},{}}, quote 
        return -(+(^(A::Array{Face,2},3)::Array{Face,2},.*(2,A::Array{Face,2})::None)::None,1)::None
    end)))
```

In \[55\]:

```
foo(A) = a_more_complicated_function(det(evaluate_a_polynomial(A)))
code_typed(foo,(typeof(A),))
```

Out\[55\]:

```
1-element Array{Any,1}:
 :($(Expr(:lambda, {:A}, {{},{{:A,Array{Face,2},0}},{}}, quote  # In[55], line 1:
        return a_more_complicated_function(det(-(+(^(A::Array{Face,2},3)::Array{Face,2},.*(2,A::Array{Face,2})::None)::None,1)::None)::None)::None
    end)))
```

# LLVM IR Generation[¶](#LLVM-IR-Generation)

In \[56\]:

```
code_llvm(evaluate_a_polynomial,(typeof(a),))
```

```
; Function Attrs: sspreq
define %ModInt @julia_evaluate_a_polynomial(%ModInt) #2 {
top:
  %1 = call %ModInt @julia_power_by_squaring6226(%ModInt %0, i64 6), !dbg !28559, !julia_type !28564
  %2 = extractvalue %ModInt %1, 0, !dbg !28559
  %3 = mul i64 %2, 3, !dbg !28559
  %4 = srem i64 %3, 11, !dbg !28559
  %5 = call %ModInt @julia_power_by_squaring6226(%ModInt %0, i64 2), !dbg !28559, !julia_type !28564
  %6 = extractvalue %ModInt %5, 0, !dbg !28559
  %7 = mul i64 %6, 3, !dbg !28559
  %8 = srem i64 %7, 11, !dbg !28559
  %9 = add i64 %8, %4, !dbg !28559
  %10 = srem i64 %9, 11, !dbg !28559
  %11 = extractvalue %ModInt %0, 0, !dbg !28559
  %12 = shl i64 %11, 1, !dbg !28559
  %13 = srem i64 %12, 11, !dbg !28559
  %14 = add i64 %13, %10, !dbg !28559
  %15 = srem i64 %14, 11, !dbg !28559
  %16 = add i64 %15, 3, !dbg !28559
  %17 = srem i64 %16, 11, !dbg !28559
  %18 = insertvalue %ModInt undef, i64 %17, 0, !dbg !28559, !julia_type !28564
  ret %ModInt %18, !dbg !28559
}
```

In \[57\]:

```
code_llvm(evaluate_a_polynomial,(typeof(A),))
```

```
; Function Attrs: sspreq
define %jl_value_t* @julia_evaluate_a_polynomial6230(%jl_value_t*, %jl_value_t**, i32) #2 {
top:
  %3 = alloca [4 x %jl_value_t*], align 8
  %.sub = getelementptr inbounds [4 x %jl_value_t*]* %3, i64 0, i64 0
  %4 = getelementptr [4 x %jl_value_t*]* %3, i64 0, i64 2, !dbg !28571
  store %jl_value_t* inttoptr (i64 4 to %jl_value_t*), %jl_value_t** %.sub, align 8
  %5 = load %jl_value_t*** @jl_pgcstack, align 8, !dbg !28571
  %6 = getelementptr [4 x %jl_value_t*]* %3, i64 0, i64 1, !dbg !28571
  %.c = bitcast %jl_value_t** %5 to %jl_value_t*, !dbg !28571
  store %jl_value_t* %.c, %jl_value_t** %6, align 8, !dbg !28571
  store %jl_value_t** %.sub, %jl_value_t*** @jl_pgcstack, align 8, !dbg !28571
  store %jl_value_t* null, %jl_value_t** %4, align 8
  %7 = getelementptr [4 x %jl_value_t*]* %3, i64 0, i64 3
  store %jl_value_t* null, %jl_value_t** %7, align 8
  %8 = load %jl_value_t** %1, align 8, !dbg !28571
  %9 = call %jl_value_t* @"julia_^6025"(%jl_value_t* %8, i64 3), !dbg !28571
  store %jl_value_t* %9, %jl_value_t** %4, align 8, !dbg !28571
  call void @"julia_.*6231"(i64 2, %jl_value_t* %8), !dbg !28571
  store %jl_value_t* inttoptr (i64 140620606479776 to %jl_value_t*), %jl_value_t** %7, align 8, !dbg !28571
  %10 = call %jl_value_t* @jl_apply_generic(%jl_value_t* inttoptr (i64 140620629152784 to %jl_value_t*), %jl_value_t** %4, i32 2), !dbg !28571
  store %jl_value_t* %10, %jl_value_t** %4, align 8, !dbg !28571
  store %jl_value_t* inttoptr (i64 140620605942320 to %jl_value_t*), %jl_value_t** %7, align 8, !dbg !28571
  %11 = call %jl_value_t* @jl_apply_generic(%jl_value_t* inttoptr (i64 140620629567872 to %jl_value_t*), %jl_value_t** %4, i32 2), !dbg !28571
  %12 = load %jl_value_t** %6, align 8, !dbg !28571
  %13 = getelementptr inbounds %jl_value_t* %12, i64 0, i32 0, !dbg !28571
  store %jl_value_t** %13, %jl_value_t*** @jl_pgcstack, align 8, !dbg !28571
  ret %jl_value_t* %11, !dbg !28571
}
```

In \[58\]:

```
code_native(evaluate_a_polynomial,(typeof(A),))
```

```
.section	__TEXT,__text,regular,pure_instructions
Filename: no file
Source line: 0
	push	rbp
	mov	rbp, rsp
	push	r15
	push	r14
	push	r12
	push	rbx
	sub	rsp, 48
	movabs	r14, 4348774360
	mov	rax, qword ptr [r14]
	mov	qword ptr [rbp - 40], rax
	mov	qword ptr [rbp - 72], 4
Source line: 0
	movabs	r15, 4348775232
	mov	rax, qword ptr [r15]
	mov	qword ptr [rbp - 64], rax
	lea	rax, qword ptr [rbp - 72]
	mov	qword ptr [r15], rax
	vxorps	xmm0, xmm0, xmm0
	vmovups	xmmword ptr [rbp - 56], xmm0
	movabs	rax, 4380607552
	mov	rbx, qword ptr [rsi]
	mov	rdi, rbx
	mov	esi, 3
	call	rax
	movabs	rcx, 4380609184
	mov	qword ptr [rbp - 56], rax
	mov	edi, 2
	mov	rsi, rbx
	call	rcx
	lea	rbx, qword ptr [rbp - 56]
	movabs	r12, 4318407168
	movabs	rax, 140620606479776
	mov	qword ptr [rbp - 48], rax
	movabs	rdi, 140620629152784
	mov	rsi, rbx
	mov	edx, 2
	call	r12
	movabs	rcx, 140620605942320
	mov	qword ptr [rbp - 56], rax
	mov	qword ptr [rbp - 48], rcx
	movabs	rdi, 140620629567872
	mov	rsi, rbx
	mov	edx, 2
	call	r12
	mov	rcx, qword ptr [rbp - 64]
	mov	qword ptr [r15], rcx
	mov	rcx, qword ptr [r14]
	cmp	rcx, qword ptr [rbp - 40]
	jne	13
	add	rsp, 48
	pop	rbx
	pop	r12
	pop	r14
	pop	r15
	pop	rbp
	ret
	movabs	rax, 140735631254601
	call	rax
```

### Calling C and Fortran[¶](#Calling-C-and-Fortran)

In \[59\]:

```
pid() = ccall(:getpid, Int32, ())
```

Out\[59\]:

```
pid (generic function with 1 method)
```

In \[60\]:

```
pid()
```

Out\[60\]:

```
46441
```

In \[61\]:

```
code_llvm(pid,())
```

```
; Function Attrs: sspreq
define i32 @julia_pid6253() #2 {
top:
  %0 = call i32 @getpid(), !dbg !28644
  ret i32 %0, !dbg !28644
}
```

# Integrating LLVM and Julia[¶](#Integrating-LLVM-and-Julia)

In \[62\]:

```
import Base.llvmcall
simd(x::NTuple{4,Int64}) = llvmcall(
"""
%3 = add <4 x i64> %1, %0
ret <4 x i64> %3
""",NTuple{4,Int64},(NTuple{4,Int64},NTuple{4,Int64}),(1,2,3,4),x)
```

Out\[62\]:

```
simd (generic function with 1 method)
```

In \[63\]:

```
simd((2,3,4,5))
```

Out\[63\]:

```
(3,5,7,9)
```

In \[64\]:

```
code_llvm(simd,(NTuple{4,Int64},))
```

```
; Function Attrs: sspreq
define <4 x i64> @julia_simd6273(<4 x i64>) #2 {
top:
  %1 = add <4 x i64> %0, &lt;i64 1, i64 2, i64 3, i64 4&gt;
  ret <4 x i64> %1, !dbg !28729
}
```

In \[65\]:

```
code_native(simd,(NTuple{4,Int64},))
```

```
.section	__TEXT,__text,regular,pure_instructions
Filename: In[62]
Source line: 2
	push	rbp
	mov	rbp, rsp
	sub	rsp, 16
	movabs	rax, 4348774360
	mov	rcx, qword ptr [rax]
	mov	qword ptr [rbp - 8], rcx
	movabs	rcx, 4624115088
	vpaddq	xmm1, xmm0, xmmword ptr [rcx]
	mov	rax, qword ptr [rax]
	cmp	rax, qword ptr [rbp - 8]
	jne	32
	vextractf128	xmm0, ymm0, 1
	movabs	rax, 4624115072
	vpaddq	xmm0, xmm0, xmmword ptr [rax]
	vinsertf128	ymm0, ymm1, xmm0, 1
Source line: 2
	add	rsp, 16
	pop	rbp
	ret
	movabs	rax, 140735631254601
	vzeroupper
	call	rax
```

In \[66\]:

<!-- MathJax configuration --> <!-- End of mathjax configuration -->
