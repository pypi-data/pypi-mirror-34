All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Description-Content-Type: UNKNOWN
Description: ======
         Hask
        ======
        
        .. image:: https://travis-ci.org/mvaled/hask.svg
        
        
        Hask is a pure-Python, zero-dependencies library that mimics most of the core
        language tools from Haskell, including:
        
        * Full Hindley-Milner type system (with typeclasses) that will typecheck any
          function decorated with a Hask type signature
        
        * Easy creation of new algebraic data types and new typeclasses, with
          Haskell-like syntax
        
        * Pattern matching with `case` expressions
        
        * Automagical function currying/partial application and function composition
        
        * Efficient, immutable, lazily evaluated `List` type with Haskell-style list
          comprehensions
        
        * All your favorite syntax and control flow tools, including operator
          sections, monadic error handling, guards, and more
        
        * Python port of (some of) the standard libraries from Haskell's `base`,
          including:
        
          * Algebraic datatypes from the Haskell `Prelude`, including `Maybe` and
            `Either`
        
          * Typeclasses from the Haskell `base` libraries, including `Functor`,
            `Applicative`, `Monad`, `Enum`, `Num`, and all the rest
        
          * Standard library functions from `base`, including all functions from
            `Prelude`, `Data.List`, `Data.Maybe`, and more
        
        
        Features not yet implemented, but coming soon:
        
        * Better support for polymorphic return values/type defaulting
        
        * Better support for lazy evaluation (beyond just the `List` type and pattern
          matching)
        
        * More of the Haskell standard library (`Control.*` libraries, QuickCheck, and
          more)
        
        * Monadic, lazy I/O
        
        .. warning:: Note that all of this is still very much pre-alpha, and some
                     things may be buggy!
        
        
        Credits
        =======
        
        This is a fork of `hask <https://github.com/billmurphy/hask_>`__ modified to
        run in Python 3.4+.
        
        See the `LICENSE file <https://github.com/mvaled/hask/blob/master/LICENSE_>`__
        keeps the original author and rights.
        
        Changes are copyright `Merchise Autrement [~º/~] and Contributors`, but with
        the same
        
Platform: UNKNOWN
Classifier: Development Status :: 2 - Pre-Alpha
Classifier: Intended Audience :: Developers
Classifier: Natural Language :: English
Classifier: License :: OSI Approved :: BSD License
Classifier: Programming Language :: Python
Classifier: Programming Language :: Python :: 2.7
Classifier: Programming Language :: Python :: 3.6
