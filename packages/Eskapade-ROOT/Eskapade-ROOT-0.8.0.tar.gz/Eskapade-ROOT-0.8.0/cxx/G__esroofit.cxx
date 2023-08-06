// Do NOT change. Changes will be lost next time file is generated

#define R__DICTIONARY_FILENAME G__esroofit

/*******************************************************************/
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#define G__DICTIONARY
#include "RConfig.h"
#include "TClass.h"
#include "TDictAttributeMap.h"
#include "TInterpreter.h"
#include "TROOT.h"
#include "TBuffer.h"
#include "TMemberInspector.h"
#include "TInterpreter.h"
#include "TVirtualMutex.h"
#include "TError.h"

#ifndef G__ROOT
#define G__ROOT
#endif

#include "RtypesImp.h"
#include "TIsAProxy.h"
#include "TFileMergeInfo.h"
#include <algorithm>
#include "TCollectionProxyInfo.h"
/*******************************************************************/

#include "TDataMember.h"

// Since CINT ignores the std namespace, we need to do so in this file.
namespace std {} using namespace std;

// Header files passed as explicit arguments
#include "esroofit/ABCDUtils.h"
#include "esroofit/DataUtils.h"
#include "esroofit/DrawUtils.h"
#include "esroofit/RhhNDKeysPdf.h"
#include "esroofit/RooABCDHistPdf.h"
#include "esroofit/RooBurr.h"
#include "esroofit/RooComplementCoef.h"
#include "esroofit/RooExpandedFitResult.h"
#include "esroofit/RooNonCentralBinning.h"
#include "esroofit/RooParamHistPdf.h"
#include "esroofit/RooTruncExponential.h"
#include "esroofit/RooWeibull.h"
#include "esroofit/Statistics.h"
#include "esroofit/TMsgLogger.h"

// Header files passed via #pragma extra_include

namespace Eskapade {
   namespace ROOT {
      inline ::ROOT::TGenericClassInfo *GenerateInitInstance();
      static TClass *Eskapade_Dictionary();

      // Function generating the singleton type initializer
      inline ::ROOT::TGenericClassInfo *GenerateInitInstance()
      {
         static ::ROOT::TGenericClassInfo 
            instance("Eskapade", 0 /*version*/, "esroofit/RooABCDHistPdf.h", 71,
                     ::ROOT::Internal::DefineBehavior((void*)0,(void*)0),
                     &Eskapade_Dictionary, 0);
         return &instance;
      }
      // Insure that the inline function is _not_ optimized away by the compiler
      ::ROOT::TGenericClassInfo *(*_R__UNIQUE_DICT_(InitFunctionKeeper))() = &GenerateInitInstance;  
      // Static variable to force the class initialization
      static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstance(); R__UseDummy(_R__UNIQUE_DICT_(Init));

      // Dictionary for non-ClassDef classes
      static TClass *Eskapade_Dictionary() {
         return GenerateInitInstance()->GetClass();
      }

   }
}

namespace Eskapade {
   namespace ABCD {
   namespace ROOT {
      inline ::ROOT::TGenericClassInfo *GenerateInitInstance();
      static TClass *EskapadecLcLABCD_Dictionary();

      // Function generating the singleton type initializer
      inline ::ROOT::TGenericClassInfo *GenerateInitInstance()
      {
         static ::ROOT::TGenericClassInfo 
            instance("Eskapade::ABCD", 0 /*version*/, "esroofit/RooABCDHistPdf.h", 73,
                     ::ROOT::Internal::DefineBehavior((void*)0,(void*)0),
                     &EskapadecLcLABCD_Dictionary, 0);
         return &instance;
      }
      // Insure that the inline function is _not_ optimized away by the compiler
      ::ROOT::TGenericClassInfo *(*_R__UNIQUE_DICT_(InitFunctionKeeper))() = &GenerateInitInstance;  
      // Static variable to force the class initialization
      static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstance(); R__UseDummy(_R__UNIQUE_DICT_(Init));

      // Dictionary for non-ClassDef classes
      static TClass *EskapadecLcLABCD_Dictionary() {
         return GenerateInitInstance()->GetClass();
      }

   }
}
}

namespace ROOT {
   static void delete_RooParamHistPdf(void *p);
   static void deleteArray_RooParamHistPdf(void *p);
   static void destruct_RooParamHistPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooParamHistPdf*)
   {
      ::RooParamHistPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooParamHistPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooParamHistPdf", ::RooParamHistPdf::Class_Version(), "esroofit/RooParamHistPdf.h", 50,
                  typeid(::RooParamHistPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooParamHistPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooParamHistPdf) );
      instance.SetDelete(&delete_RooParamHistPdf);
      instance.SetDeleteArray(&deleteArray_RooParamHistPdf);
      instance.SetDestructor(&destruct_RooParamHistPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooParamHistPdf*)
   {
      return GenerateInitInstanceLocal((::RooParamHistPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooParamHistPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_RooABCDHistPdf(void *p);
   static void deleteArray_RooABCDHistPdf(void *p);
   static void destruct_RooABCDHistPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooABCDHistPdf*)
   {
      ::RooABCDHistPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooABCDHistPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooABCDHistPdf", ::RooABCDHistPdf::Class_Version(), "esroofit/RooABCDHistPdf.h", 80,
                  typeid(::RooABCDHistPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooABCDHistPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RooABCDHistPdf) );
      instance.SetDelete(&delete_RooABCDHistPdf);
      instance.SetDeleteArray(&deleteArray_RooABCDHistPdf);
      instance.SetDestructor(&destruct_RooABCDHistPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooABCDHistPdf*)
   {
      return GenerateInitInstanceLocal((::RooABCDHistPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooABCDHistPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_RhhNDKeysPdf(void *p);
   static void deleteArray_RhhNDKeysPdf(void *p);
   static void destruct_RhhNDKeysPdf(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RhhNDKeysPdf*)
   {
      ::RhhNDKeysPdf *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RhhNDKeysPdf >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RhhNDKeysPdf", ::RhhNDKeysPdf::Class_Version(), "esroofit/RhhNDKeysPdf.h", 42,
                  typeid(::RhhNDKeysPdf), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RhhNDKeysPdf::Dictionary, isa_proxy, 4,
                  sizeof(::RhhNDKeysPdf) );
      instance.SetDelete(&delete_RhhNDKeysPdf);
      instance.SetDeleteArray(&deleteArray_RhhNDKeysPdf);
      instance.SetDestructor(&destruct_RhhNDKeysPdf);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RhhNDKeysPdf*)
   {
      return GenerateInitInstanceLocal((::RhhNDKeysPdf*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RhhNDKeysPdf*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooBurr(void *p = 0);
   static void *newArray_RooBurr(Long_t size, void *p);
   static void delete_RooBurr(void *p);
   static void deleteArray_RooBurr(void *p);
   static void destruct_RooBurr(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooBurr*)
   {
      ::RooBurr *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooBurr >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooBurr", ::RooBurr::Class_Version(), "esroofit/RooBurr.h", 15,
                  typeid(::RooBurr), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooBurr::Dictionary, isa_proxy, 4,
                  sizeof(::RooBurr) );
      instance.SetNew(&new_RooBurr);
      instance.SetNewArray(&newArray_RooBurr);
      instance.SetDelete(&delete_RooBurr);
      instance.SetDeleteArray(&deleteArray_RooBurr);
      instance.SetDestructor(&destruct_RooBurr);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooBurr*)
   {
      return GenerateInitInstanceLocal((::RooBurr*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooBurr*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooComplementCoef(void *p = 0);
   static void *newArray_RooComplementCoef(Long_t size, void *p);
   static void delete_RooComplementCoef(void *p);
   static void deleteArray_RooComplementCoef(void *p);
   static void destruct_RooComplementCoef(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooComplementCoef*)
   {
      ::RooComplementCoef *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooComplementCoef >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooComplementCoef", ::RooComplementCoef::Class_Version(), "esroofit/RooComplementCoef.h", 24,
                  typeid(::RooComplementCoef), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooComplementCoef::Dictionary, isa_proxy, 4,
                  sizeof(::RooComplementCoef) );
      instance.SetNew(&new_RooComplementCoef);
      instance.SetNewArray(&newArray_RooComplementCoef);
      instance.SetDelete(&delete_RooComplementCoef);
      instance.SetDeleteArray(&deleteArray_RooComplementCoef);
      instance.SetDestructor(&destruct_RooComplementCoef);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooComplementCoef*)
   {
      return GenerateInitInstanceLocal((::RooComplementCoef*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooComplementCoef*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void delete_RooExpandedFitResult(void *p);
   static void deleteArray_RooExpandedFitResult(void *p);
   static void destruct_RooExpandedFitResult(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooExpandedFitResult*)
   {
      ::RooExpandedFitResult *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooExpandedFitResult >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooExpandedFitResult", ::RooExpandedFitResult::Class_Version(), "esroofit/RooExpandedFitResult.h", 38,
                  typeid(::RooExpandedFitResult), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooExpandedFitResult::Dictionary, isa_proxy, 4,
                  sizeof(::RooExpandedFitResult) );
      instance.SetDelete(&delete_RooExpandedFitResult);
      instance.SetDeleteArray(&deleteArray_RooExpandedFitResult);
      instance.SetDestructor(&destruct_RooExpandedFitResult);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooExpandedFitResult*)
   {
      return GenerateInitInstanceLocal((::RooExpandedFitResult*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooExpandedFitResult*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooNonCentralBinning(void *p = 0);
   static void *newArray_RooNonCentralBinning(Long_t size, void *p);
   static void delete_RooNonCentralBinning(void *p);
   static void deleteArray_RooNonCentralBinning(void *p);
   static void destruct_RooNonCentralBinning(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooNonCentralBinning*)
   {
      ::RooNonCentralBinning *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooNonCentralBinning >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooNonCentralBinning", ::RooNonCentralBinning::Class_Version(), "esroofit/RooNonCentralBinning.h", 38,
                  typeid(::RooNonCentralBinning), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooNonCentralBinning::Dictionary, isa_proxy, 4,
                  sizeof(::RooNonCentralBinning) );
      instance.SetNew(&new_RooNonCentralBinning);
      instance.SetNewArray(&newArray_RooNonCentralBinning);
      instance.SetDelete(&delete_RooNonCentralBinning);
      instance.SetDeleteArray(&deleteArray_RooNonCentralBinning);
      instance.SetDestructor(&destruct_RooNonCentralBinning);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooNonCentralBinning*)
   {
      return GenerateInitInstanceLocal((::RooNonCentralBinning*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooNonCentralBinning*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooTruncExponential(void *p = 0);
   static void *newArray_RooTruncExponential(Long_t size, void *p);
   static void delete_RooTruncExponential(void *p);
   static void deleteArray_RooTruncExponential(void *p);
   static void destruct_RooTruncExponential(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooTruncExponential*)
   {
      ::RooTruncExponential *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooTruncExponential >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooTruncExponential", ::RooTruncExponential::Class_Version(), "esroofit/RooTruncExponential.h", 31,
                  typeid(::RooTruncExponential), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooTruncExponential::Dictionary, isa_proxy, 4,
                  sizeof(::RooTruncExponential) );
      instance.SetNew(&new_RooTruncExponential);
      instance.SetNewArray(&newArray_RooTruncExponential);
      instance.SetDelete(&delete_RooTruncExponential);
      instance.SetDeleteArray(&deleteArray_RooTruncExponential);
      instance.SetDestructor(&destruct_RooTruncExponential);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooTruncExponential*)
   {
      return GenerateInitInstanceLocal((::RooTruncExponential*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooTruncExponential*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_RooWeibull(void *p = 0);
   static void *newArray_RooWeibull(Long_t size, void *p);
   static void delete_RooWeibull(void *p);
   static void deleteArray_RooWeibull(void *p);
   static void destruct_RooWeibull(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::RooWeibull*)
   {
      ::RooWeibull *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::RooWeibull >(0);
      static ::ROOT::TGenericClassInfo 
         instance("RooWeibull", ::RooWeibull::Class_Version(), "esroofit/RooWeibull.h", 36,
                  typeid(::RooWeibull), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::RooWeibull::Dictionary, isa_proxy, 4,
                  sizeof(::RooWeibull) );
      instance.SetNew(&new_RooWeibull);
      instance.SetNewArray(&newArray_RooWeibull);
      instance.SetDelete(&delete_RooWeibull);
      instance.SetDeleteArray(&deleteArray_RooWeibull);
      instance.SetDestructor(&destruct_RooWeibull);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::RooWeibull*)
   {
      return GenerateInitInstanceLocal((::RooWeibull*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::RooWeibull*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

namespace ROOT {
   static void *new_TMsgLogger(void *p = 0);
   static void *newArray_TMsgLogger(Long_t size, void *p);
   static void delete_TMsgLogger(void *p);
   static void deleteArray_TMsgLogger(void *p);
   static void destruct_TMsgLogger(void *p);
   static void streamer_TMsgLogger(TBuffer &buf, void *obj);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const ::TMsgLogger*)
   {
      ::TMsgLogger *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TInstrumentedIsAProxy< ::TMsgLogger >(0);
      static ::ROOT::TGenericClassInfo 
         instance("TMsgLogger", ::TMsgLogger::Class_Version(), "esroofit/TMsgLogger.h", 62,
                  typeid(::TMsgLogger), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &::TMsgLogger::Dictionary, isa_proxy, 16,
                  sizeof(::TMsgLogger) );
      instance.SetNew(&new_TMsgLogger);
      instance.SetNewArray(&newArray_TMsgLogger);
      instance.SetDelete(&delete_TMsgLogger);
      instance.SetDeleteArray(&deleteArray_TMsgLogger);
      instance.SetDestructor(&destruct_TMsgLogger);
      instance.SetStreamerFunc(&streamer_TMsgLogger);
      return &instance;
   }
   TGenericClassInfo *GenerateInitInstance(const ::TMsgLogger*)
   {
      return GenerateInitInstanceLocal((::TMsgLogger*)0);
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const ::TMsgLogger*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));
} // end of namespace ROOT

//______________________________________________________________________________
atomic_TClass_ptr RooParamHistPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooParamHistPdf::Class_Name()
{
   return "RooParamHistPdf";
}

//______________________________________________________________________________
const char *RooParamHistPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParamHistPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooParamHistPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooParamHistPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooParamHistPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParamHistPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooParamHistPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooParamHistPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooABCDHistPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooABCDHistPdf::Class_Name()
{
   return "RooABCDHistPdf";
}

//______________________________________________________________________________
const char *RooABCDHistPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooABCDHistPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooABCDHistPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooABCDHistPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooABCDHistPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooABCDHistPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooABCDHistPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooABCDHistPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RhhNDKeysPdf::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RhhNDKeysPdf::Class_Name()
{
   return "RhhNDKeysPdf";
}

//______________________________________________________________________________
const char *RhhNDKeysPdf::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RhhNDKeysPdf*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RhhNDKeysPdf::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RhhNDKeysPdf*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RhhNDKeysPdf::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RhhNDKeysPdf*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RhhNDKeysPdf::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RhhNDKeysPdf*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooBurr::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooBurr::Class_Name()
{
   return "RooBurr";
}

//______________________________________________________________________________
const char *RooBurr::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBurr*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooBurr::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooBurr*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooBurr::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBurr*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooBurr::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooBurr*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooComplementCoef::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooComplementCoef::Class_Name()
{
   return "RooComplementCoef";
}

//______________________________________________________________________________
const char *RooComplementCoef::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooComplementCoef*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooComplementCoef::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooComplementCoef*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooComplementCoef::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooComplementCoef*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooComplementCoef::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooComplementCoef*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooExpandedFitResult::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooExpandedFitResult::Class_Name()
{
   return "RooExpandedFitResult";
}

//______________________________________________________________________________
const char *RooExpandedFitResult::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpandedFitResult*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooExpandedFitResult::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooExpandedFitResult*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooExpandedFitResult::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpandedFitResult*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooExpandedFitResult::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooExpandedFitResult*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooNonCentralBinning::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooNonCentralBinning::Class_Name()
{
   return "RooNonCentralBinning";
}

//______________________________________________________________________________
const char *RooNonCentralBinning::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNonCentralBinning*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooNonCentralBinning::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooNonCentralBinning*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooNonCentralBinning::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNonCentralBinning*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooNonCentralBinning::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooNonCentralBinning*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooTruncExponential::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooTruncExponential::Class_Name()
{
   return "RooTruncExponential";
}

//______________________________________________________________________________
const char *RooTruncExponential::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTruncExponential*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooTruncExponential::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooTruncExponential*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooTruncExponential::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTruncExponential*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooTruncExponential::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooTruncExponential*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr RooWeibull::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *RooWeibull::Class_Name()
{
   return "RooWeibull";
}

//______________________________________________________________________________
const char *RooWeibull::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooWeibull*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int RooWeibull::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::RooWeibull*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *RooWeibull::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooWeibull*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *RooWeibull::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::RooWeibull*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
atomic_TClass_ptr TMsgLogger::fgIsA(0);  // static to hold class pointer

//______________________________________________________________________________
const char *TMsgLogger::Class_Name()
{
   return "TMsgLogger";
}

//______________________________________________________________________________
const char *TMsgLogger::ImplFileName()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::TMsgLogger*)0x0)->GetImplFileName();
}

//______________________________________________________________________________
int TMsgLogger::ImplFileLine()
{
   return ::ROOT::GenerateInitInstanceLocal((const ::TMsgLogger*)0x0)->GetImplFileLine();
}

//______________________________________________________________________________
TClass *TMsgLogger::Dictionary()
{
   fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::TMsgLogger*)0x0)->GetClass();
   return fgIsA;
}

//______________________________________________________________________________
TClass *TMsgLogger::Class()
{
   if (!fgIsA.load()) { R__LOCKGUARD2(gInterpreterMutex); fgIsA = ::ROOT::GenerateInitInstanceLocal((const ::TMsgLogger*)0x0)->GetClass(); }
   return fgIsA;
}

//______________________________________________________________________________
void RooParamHistPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooParamHistPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooParamHistPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooParamHistPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_RooParamHistPdf(void *p) {
      delete ((::RooParamHistPdf*)p);
   }
   static void deleteArray_RooParamHistPdf(void *p) {
      delete [] ((::RooParamHistPdf*)p);
   }
   static void destruct_RooParamHistPdf(void *p) {
      typedef ::RooParamHistPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooParamHistPdf

//______________________________________________________________________________
void RooABCDHistPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooABCDHistPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooABCDHistPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooABCDHistPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_RooABCDHistPdf(void *p) {
      delete ((::RooABCDHistPdf*)p);
   }
   static void deleteArray_RooABCDHistPdf(void *p) {
      delete [] ((::RooABCDHistPdf*)p);
   }
   static void destruct_RooABCDHistPdf(void *p) {
      typedef ::RooABCDHistPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooABCDHistPdf

//______________________________________________________________________________
void RhhNDKeysPdf::Streamer(TBuffer &R__b)
{
   // Stream an object of class RhhNDKeysPdf.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RhhNDKeysPdf::Class(),this);
   } else {
      R__b.WriteClassBuffer(RhhNDKeysPdf::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_RhhNDKeysPdf(void *p) {
      delete ((::RhhNDKeysPdf*)p);
   }
   static void deleteArray_RhhNDKeysPdf(void *p) {
      delete [] ((::RhhNDKeysPdf*)p);
   }
   static void destruct_RhhNDKeysPdf(void *p) {
      typedef ::RhhNDKeysPdf current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RhhNDKeysPdf

//______________________________________________________________________________
void RooBurr::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooBurr.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooBurr::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooBurr::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooBurr(void *p) {
      return  p ? new(p) ::RooBurr : new ::RooBurr;
   }
   static void *newArray_RooBurr(Long_t nElements, void *p) {
      return p ? new(p) ::RooBurr[nElements] : new ::RooBurr[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooBurr(void *p) {
      delete ((::RooBurr*)p);
   }
   static void deleteArray_RooBurr(void *p) {
      delete [] ((::RooBurr*)p);
   }
   static void destruct_RooBurr(void *p) {
      typedef ::RooBurr current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooBurr

//______________________________________________________________________________
void RooComplementCoef::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooComplementCoef.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooComplementCoef::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooComplementCoef::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooComplementCoef(void *p) {
      return  p ? new(p) ::RooComplementCoef : new ::RooComplementCoef;
   }
   static void *newArray_RooComplementCoef(Long_t nElements, void *p) {
      return p ? new(p) ::RooComplementCoef[nElements] : new ::RooComplementCoef[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooComplementCoef(void *p) {
      delete ((::RooComplementCoef*)p);
   }
   static void deleteArray_RooComplementCoef(void *p) {
      delete [] ((::RooComplementCoef*)p);
   }
   static void destruct_RooComplementCoef(void *p) {
      typedef ::RooComplementCoef current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooComplementCoef

//______________________________________________________________________________
void RooExpandedFitResult::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooExpandedFitResult.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooExpandedFitResult::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooExpandedFitResult::Class(),this);
   }
}

namespace ROOT {
   // Wrapper around operator delete
   static void delete_RooExpandedFitResult(void *p) {
      delete ((::RooExpandedFitResult*)p);
   }
   static void deleteArray_RooExpandedFitResult(void *p) {
      delete [] ((::RooExpandedFitResult*)p);
   }
   static void destruct_RooExpandedFitResult(void *p) {
      typedef ::RooExpandedFitResult current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooExpandedFitResult

//______________________________________________________________________________
void RooNonCentralBinning::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooNonCentralBinning.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooNonCentralBinning::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooNonCentralBinning::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooNonCentralBinning(void *p) {
      return  p ? new(p) ::RooNonCentralBinning : new ::RooNonCentralBinning;
   }
   static void *newArray_RooNonCentralBinning(Long_t nElements, void *p) {
      return p ? new(p) ::RooNonCentralBinning[nElements] : new ::RooNonCentralBinning[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooNonCentralBinning(void *p) {
      delete ((::RooNonCentralBinning*)p);
   }
   static void deleteArray_RooNonCentralBinning(void *p) {
      delete [] ((::RooNonCentralBinning*)p);
   }
   static void destruct_RooNonCentralBinning(void *p) {
      typedef ::RooNonCentralBinning current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooNonCentralBinning

//______________________________________________________________________________
void RooTruncExponential::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooTruncExponential.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooTruncExponential::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooTruncExponential::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooTruncExponential(void *p) {
      return  p ? new(p) ::RooTruncExponential : new ::RooTruncExponential;
   }
   static void *newArray_RooTruncExponential(Long_t nElements, void *p) {
      return p ? new(p) ::RooTruncExponential[nElements] : new ::RooTruncExponential[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooTruncExponential(void *p) {
      delete ((::RooTruncExponential*)p);
   }
   static void deleteArray_RooTruncExponential(void *p) {
      delete [] ((::RooTruncExponential*)p);
   }
   static void destruct_RooTruncExponential(void *p) {
      typedef ::RooTruncExponential current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooTruncExponential

//______________________________________________________________________________
void RooWeibull::Streamer(TBuffer &R__b)
{
   // Stream an object of class RooWeibull.

   if (R__b.IsReading()) {
      R__b.ReadClassBuffer(RooWeibull::Class(),this);
   } else {
      R__b.WriteClassBuffer(RooWeibull::Class(),this);
   }
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_RooWeibull(void *p) {
      return  p ? new(p) ::RooWeibull : new ::RooWeibull;
   }
   static void *newArray_RooWeibull(Long_t nElements, void *p) {
      return p ? new(p) ::RooWeibull[nElements] : new ::RooWeibull[nElements];
   }
   // Wrapper around operator delete
   static void delete_RooWeibull(void *p) {
      delete ((::RooWeibull*)p);
   }
   static void deleteArray_RooWeibull(void *p) {
      delete [] ((::RooWeibull*)p);
   }
   static void destruct_RooWeibull(void *p) {
      typedef ::RooWeibull current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class ::RooWeibull

//______________________________________________________________________________
void TMsgLogger::Streamer(TBuffer &R__b)
{
   // Stream an object of class TMsgLogger.

   TObject::Streamer(R__b);
}

namespace ROOT {
   // Wrappers around operator new
   static void *new_TMsgLogger(void *p) {
      return  p ? new(p) ::TMsgLogger : new ::TMsgLogger;
   }
   static void *newArray_TMsgLogger(Long_t nElements, void *p) {
      return p ? new(p) ::TMsgLogger[nElements] : new ::TMsgLogger[nElements];
   }
   // Wrapper around operator delete
   static void delete_TMsgLogger(void *p) {
      delete ((::TMsgLogger*)p);
   }
   static void deleteArray_TMsgLogger(void *p) {
      delete [] ((::TMsgLogger*)p);
   }
   static void destruct_TMsgLogger(void *p) {
      typedef ::TMsgLogger current_t;
      ((current_t*)p)->~current_t();
   }
   // Wrapper around a custom streamer member function.
   static void streamer_TMsgLogger(TBuffer &buf, void *obj) {
      ((::TMsgLogger*)obj)->::TMsgLogger::Streamer(buf);
   }
} // end of namespace ROOT for class ::TMsgLogger

namespace ROOT {
   static TClass *vectorlEvectorlEdoublegRsPgR_Dictionary();
   static void vectorlEvectorlEdoublegRsPgR_TClassManip(TClass*);
   static void *new_vectorlEvectorlEdoublegRsPgR(void *p = 0);
   static void *newArray_vectorlEvectorlEdoublegRsPgR(Long_t size, void *p);
   static void delete_vectorlEvectorlEdoublegRsPgR(void *p);
   static void deleteArray_vectorlEvectorlEdoublegRsPgR(void *p);
   static void destruct_vectorlEvectorlEdoublegRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<vector<double> >*)
   {
      vector<vector<double> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<vector<double> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<vector<double> >", -2, "vector", 214,
                  typeid(vector<vector<double> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEvectorlEdoublegRsPgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<vector<double> >) );
      instance.SetNew(&new_vectorlEvectorlEdoublegRsPgR);
      instance.SetNewArray(&newArray_vectorlEvectorlEdoublegRsPgR);
      instance.SetDelete(&delete_vectorlEvectorlEdoublegRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlEvectorlEdoublegRsPgR);
      instance.SetDestructor(&destruct_vectorlEvectorlEdoublegRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<vector<double> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<vector<double> >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEvectorlEdoublegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<vector<double> >*)0x0)->GetClass();
      vectorlEvectorlEdoublegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEvectorlEdoublegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEvectorlEdoublegRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<double> > : new vector<vector<double> >;
   }
   static void *newArray_vectorlEvectorlEdoublegRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<vector<double> >[nElements] : new vector<vector<double> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEvectorlEdoublegRsPgR(void *p) {
      delete ((vector<vector<double> >*)p);
   }
   static void deleteArray_vectorlEvectorlEdoublegRsPgR(void *p) {
      delete [] ((vector<vector<double> >*)p);
   }
   static void destruct_vectorlEvectorlEdoublegRsPgR(void *p) {
      typedef vector<vector<double> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<vector<double> >

namespace ROOT {
   static TClass *vectorlEstringgR_Dictionary();
   static void vectorlEstringgR_TClassManip(TClass*);
   static void *new_vectorlEstringgR(void *p = 0);
   static void *newArray_vectorlEstringgR(Long_t size, void *p);
   static void delete_vectorlEstringgR(void *p);
   static void deleteArray_vectorlEstringgR(void *p);
   static void destruct_vectorlEstringgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<string>*)
   {
      vector<string> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<string>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<string>", -2, "vector", 214,
                  typeid(vector<string>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEstringgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<string>) );
      instance.SetNew(&new_vectorlEstringgR);
      instance.SetNewArray(&newArray_vectorlEstringgR);
      instance.SetDelete(&delete_vectorlEstringgR);
      instance.SetDeleteArray(&deleteArray_vectorlEstringgR);
      instance.SetDestructor(&destruct_vectorlEstringgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<string> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<string>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEstringgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<string>*)0x0)->GetClass();
      vectorlEstringgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEstringgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEstringgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<string> : new vector<string>;
   }
   static void *newArray_vectorlEstringgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<string>[nElements] : new vector<string>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEstringgR(void *p) {
      delete ((vector<string>*)p);
   }
   static void deleteArray_vectorlEstringgR(void *p) {
      delete [] ((vector<string>*)p);
   }
   static void destruct_vectorlEstringgR(void *p) {
      typedef vector<string> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<string>

namespace ROOT {
   static TClass *vectorlEintgR_Dictionary();
   static void vectorlEintgR_TClassManip(TClass*);
   static void *new_vectorlEintgR(void *p = 0);
   static void *newArray_vectorlEintgR(Long_t size, void *p);
   static void delete_vectorlEintgR(void *p);
   static void deleteArray_vectorlEintgR(void *p);
   static void destruct_vectorlEintgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<int>*)
   {
      vector<int> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<int>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<int>", -2, "vector", 214,
                  typeid(vector<int>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEintgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<int>) );
      instance.SetNew(&new_vectorlEintgR);
      instance.SetNewArray(&newArray_vectorlEintgR);
      instance.SetDelete(&delete_vectorlEintgR);
      instance.SetDeleteArray(&deleteArray_vectorlEintgR);
      instance.SetDestructor(&destruct_vectorlEintgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<int> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<int>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEintgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<int>*)0x0)->GetClass();
      vectorlEintgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEintgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEintgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<int> : new vector<int>;
   }
   static void *newArray_vectorlEintgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<int>[nElements] : new vector<int>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEintgR(void *p) {
      delete ((vector<int>*)p);
   }
   static void deleteArray_vectorlEintgR(void *p) {
      delete [] ((vector<int>*)p);
   }
   static void destruct_vectorlEintgR(void *p) {
      typedef vector<int> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<int>

namespace ROOT {
   static TClass *vectorlEdoublegR_Dictionary();
   static void vectorlEdoublegR_TClassManip(TClass*);
   static void *new_vectorlEdoublegR(void *p = 0);
   static void *newArray_vectorlEdoublegR(Long_t size, void *p);
   static void delete_vectorlEdoublegR(void *p);
   static void deleteArray_vectorlEdoublegR(void *p);
   static void destruct_vectorlEdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<double>*)
   {
      vector<double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<double>));
      static ::ROOT::TGenericClassInfo 
         instance("vector<double>", -2, "vector", 214,
                  typeid(vector<double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlEdoublegR_Dictionary, isa_proxy, 0,
                  sizeof(vector<double>) );
      instance.SetNew(&new_vectorlEdoublegR);
      instance.SetNewArray(&newArray_vectorlEdoublegR);
      instance.SetDelete(&delete_vectorlEdoublegR);
      instance.SetDeleteArray(&deleteArray_vectorlEdoublegR);
      instance.SetDestructor(&destruct_vectorlEdoublegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<double> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlEdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<double>*)0x0)->GetClass();
      vectorlEdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlEdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlEdoublegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<double> : new vector<double>;
   }
   static void *newArray_vectorlEdoublegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<double>[nElements] : new vector<double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlEdoublegR(void *p) {
      delete ((vector<double>*)p);
   }
   static void deleteArray_vectorlEdoublegR(void *p) {
      delete [] ((vector<double>*)p);
   }
   static void destruct_vectorlEdoublegR(void *p) {
      typedef vector<double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<double>

namespace ROOT {
   static TClass *vectorlETVectorTlEdoublegRsPgR_Dictionary();
   static void vectorlETVectorTlEdoublegRsPgR_TClassManip(TClass*);
   static void *new_vectorlETVectorTlEdoublegRsPgR(void *p = 0);
   static void *newArray_vectorlETVectorTlEdoublegRsPgR(Long_t size, void *p);
   static void delete_vectorlETVectorTlEdoublegRsPgR(void *p);
   static void deleteArray_vectorlETVectorTlEdoublegRsPgR(void *p);
   static void destruct_vectorlETVectorTlEdoublegRsPgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const vector<TVectorT<double> >*)
   {
      vector<TVectorT<double> > *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(vector<TVectorT<double> >));
      static ::ROOT::TGenericClassInfo 
         instance("vector<TVectorT<double> >", -2, "vector", 214,
                  typeid(vector<TVectorT<double> >), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &vectorlETVectorTlEdoublegRsPgR_Dictionary, isa_proxy, 0,
                  sizeof(vector<TVectorT<double> >) );
      instance.SetNew(&new_vectorlETVectorTlEdoublegRsPgR);
      instance.SetNewArray(&newArray_vectorlETVectorTlEdoublegRsPgR);
      instance.SetDelete(&delete_vectorlETVectorTlEdoublegRsPgR);
      instance.SetDeleteArray(&deleteArray_vectorlETVectorTlEdoublegRsPgR);
      instance.SetDestructor(&destruct_vectorlETVectorTlEdoublegRsPgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::Pushback< vector<TVectorT<double> > >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const vector<TVectorT<double> >*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *vectorlETVectorTlEdoublegRsPgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const vector<TVectorT<double> >*)0x0)->GetClass();
      vectorlETVectorTlEdoublegRsPgR_TClassManip(theClass);
   return theClass;
   }

   static void vectorlETVectorTlEdoublegRsPgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_vectorlETVectorTlEdoublegRsPgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<TVectorT<double> > : new vector<TVectorT<double> >;
   }
   static void *newArray_vectorlETVectorTlEdoublegRsPgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) vector<TVectorT<double> >[nElements] : new vector<TVectorT<double> >[nElements];
   }
   // Wrapper around operator delete
   static void delete_vectorlETVectorTlEdoublegRsPgR(void *p) {
      delete ((vector<TVectorT<double> >*)p);
   }
   static void deleteArray_vectorlETVectorTlEdoublegRsPgR(void *p) {
      delete [] ((vector<TVectorT<double> >*)p);
   }
   static void destruct_vectorlETVectorTlEdoublegRsPgR(void *p) {
      typedef vector<TVectorT<double> > current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class vector<TVectorT<double> >

namespace ROOT {
   static TClass *maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR_Dictionary();
   static void maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR_TClassManip(TClass*);
   static void *new_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p = 0);
   static void *newArray_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(Long_t size, void *p);
   static void delete_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p);
   static void deleteArray_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p);
   static void destruct_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>*)
   {
      map<pair<string,int>,RhhNDKeysPdf::BoxInfo*> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>));
      static ::ROOT::TGenericClassInfo 
         instance("map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>", -2, "map", 96,
                  typeid(map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR_Dictionary, isa_proxy, 0,
                  sizeof(map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>) );
      instance.SetNew(&new_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR);
      instance.SetNewArray(&newArray_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR);
      instance.SetDelete(&delete_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR);
      instance.SetDeleteArray(&deleteArray_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR);
      instance.SetDestructor(&destruct_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<pair<string,int>,RhhNDKeysPdf::BoxInfo*> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>*)0x0)->GetClass();
      maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<pair<string,int>,RhhNDKeysPdf::BoxInfo*> : new map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>;
   }
   static void *newArray_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>[nElements] : new map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p) {
      delete ((map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>*)p);
   }
   static void deleteArray_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p) {
      delete [] ((map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>*)p);
   }
   static void destruct_maplEpairlEstringcOintgRcORhhNDKeysPdfcLcLBoxInfomUgR(void *p) {
      typedef map<pair<string,int>,RhhNDKeysPdf::BoxInfo*> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<pair<string,int>,RhhNDKeysPdf::BoxInfo*>

namespace ROOT {
   static TClass *maplEintcOdoublegR_Dictionary();
   static void maplEintcOdoublegR_TClassManip(TClass*);
   static void *new_maplEintcOdoublegR(void *p = 0);
   static void *newArray_maplEintcOdoublegR(Long_t size, void *p);
   static void delete_maplEintcOdoublegR(void *p);
   static void deleteArray_maplEintcOdoublegR(void *p);
   static void destruct_maplEintcOdoublegR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<int,double>*)
   {
      map<int,double> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<int,double>));
      static ::ROOT::TGenericClassInfo 
         instance("map<int,double>", -2, "map", 96,
                  typeid(map<int,double>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEintcOdoublegR_Dictionary, isa_proxy, 0,
                  sizeof(map<int,double>) );
      instance.SetNew(&new_maplEintcOdoublegR);
      instance.SetNewArray(&newArray_maplEintcOdoublegR);
      instance.SetDelete(&delete_maplEintcOdoublegR);
      instance.SetDeleteArray(&deleteArray_maplEintcOdoublegR);
      instance.SetDestructor(&destruct_maplEintcOdoublegR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<int,double> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const map<int,double>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEintcOdoublegR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<int,double>*)0x0)->GetClass();
      maplEintcOdoublegR_TClassManip(theClass);
   return theClass;
   }

   static void maplEintcOdoublegR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEintcOdoublegR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,double> : new map<int,double>;
   }
   static void *newArray_maplEintcOdoublegR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,double>[nElements] : new map<int,double>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEintcOdoublegR(void *p) {
      delete ((map<int,double>*)p);
   }
   static void deleteArray_maplEintcOdoublegR(void *p) {
      delete [] ((map<int,double>*)p);
   }
   static void destruct_maplEintcOdoublegR(void *p) {
      typedef map<int,double> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<int,double>

namespace ROOT {
   static TClass *maplEintcOboolgR_Dictionary();
   static void maplEintcOboolgR_TClassManip(TClass*);
   static void *new_maplEintcOboolgR(void *p = 0);
   static void *newArray_maplEintcOboolgR(Long_t size, void *p);
   static void delete_maplEintcOboolgR(void *p);
   static void deleteArray_maplEintcOboolgR(void *p);
   static void destruct_maplEintcOboolgR(void *p);

   // Function generating the singleton type initializer
   static TGenericClassInfo *GenerateInitInstanceLocal(const map<int,bool>*)
   {
      map<int,bool> *ptr = 0;
      static ::TVirtualIsAProxy* isa_proxy = new ::TIsAProxy(typeid(map<int,bool>));
      static ::ROOT::TGenericClassInfo 
         instance("map<int,bool>", -2, "map", 96,
                  typeid(map<int,bool>), ::ROOT::Internal::DefineBehavior(ptr, ptr),
                  &maplEintcOboolgR_Dictionary, isa_proxy, 0,
                  sizeof(map<int,bool>) );
      instance.SetNew(&new_maplEintcOboolgR);
      instance.SetNewArray(&newArray_maplEintcOboolgR);
      instance.SetDelete(&delete_maplEintcOboolgR);
      instance.SetDeleteArray(&deleteArray_maplEintcOboolgR);
      instance.SetDestructor(&destruct_maplEintcOboolgR);
      instance.AdoptCollectionProxyInfo(TCollectionProxyInfo::Generate(TCollectionProxyInfo::MapInsert< map<int,bool> >()));
      return &instance;
   }
   // Static variable to force the class initialization
   static ::ROOT::TGenericClassInfo *_R__UNIQUE_DICT_(Init) = GenerateInitInstanceLocal((const map<int,bool>*)0x0); R__UseDummy(_R__UNIQUE_DICT_(Init));

   // Dictionary for non-ClassDef classes
   static TClass *maplEintcOboolgR_Dictionary() {
      TClass* theClass =::ROOT::GenerateInitInstanceLocal((const map<int,bool>*)0x0)->GetClass();
      maplEintcOboolgR_TClassManip(theClass);
   return theClass;
   }

   static void maplEintcOboolgR_TClassManip(TClass* ){
   }

} // end of namespace ROOT

namespace ROOT {
   // Wrappers around operator new
   static void *new_maplEintcOboolgR(void *p) {
      return  p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,bool> : new map<int,bool>;
   }
   static void *newArray_maplEintcOboolgR(Long_t nElements, void *p) {
      return p ? ::new((::ROOT::Internal::TOperatorNewHelper*)p) map<int,bool>[nElements] : new map<int,bool>[nElements];
   }
   // Wrapper around operator delete
   static void delete_maplEintcOboolgR(void *p) {
      delete ((map<int,bool>*)p);
   }
   static void deleteArray_maplEintcOboolgR(void *p) {
      delete [] ((map<int,bool>*)p);
   }
   static void destruct_maplEintcOboolgR(void *p) {
      typedef map<int,bool> current_t;
      ((current_t*)p)->~current_t();
   }
} // end of namespace ROOT for class map<int,bool>

namespace {
  void TriggerDictionaryInitialization_libesroofit_Impl() {
    static const char* headers[] = {
"esroofit/ABCDUtils.h",
"esroofit/DataUtils.h",
"esroofit/DrawUtils.h",
"esroofit/RhhNDKeysPdf.h",
"esroofit/RooABCDHistPdf.h",
"esroofit/RooBurr.h",
"esroofit/RooComplementCoef.h",
"esroofit/RooExpandedFitResult.h",
"esroofit/RooNonCentralBinning.h",
"esroofit/RooParamHistPdf.h",
"esroofit/RooTruncExponential.h",
"esroofit/RooWeibull.h",
"esroofit/Statistics.h",
"esroofit/TMsgLogger.h",
0
    };
    static const char* includePaths[] = {
0
    };
    static const char* fwdDeclCode = R"DICTFWDDCLS(
#line 1 "libesroofit dictionary forward declarations' payload"
#pragma clang diagnostic ignored "-Wkeyword-compat"
#pragma clang diagnostic ignored "-Wignored-attributes"
#pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
extern int __Cling_Autoloading_Map;
class __attribute__((annotate(R"ATTRDUMP(Histogram based PDF)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$esroofit/RooParamHistPdf.h")))  __attribute__((annotate("$clingAutoload$esroofit/ABCDUtils.h")))  RooParamHistPdf;
class __attribute__((annotate(R"ATTRDUMP(Histogram based PDF)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$esroofit/RooABCDHistPdf.h")))  __attribute__((annotate("$clingAutoload$esroofit/ABCDUtils.h")))  RooABCDHistPdf;
class __attribute__((annotate(R"ATTRDUMP(General N-dimensional non-parametric kernel estimation p.d.f)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$esroofit/RhhNDKeysPdf.h")))  RhhNDKeysPdf;
class __attribute__((annotate("$clingAutoload$esroofit/RooBurr.h")))  RooBurr;
class __attribute__((annotate("$clingAutoload$esroofit/RooComplementCoef.h")))  RooComplementCoef;
class __attribute__((annotate(R"ATTRDUMP(Container class for expanded fit result)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$esroofit/RooExpandedFitResult.h")))  RooExpandedFitResult;
class __attribute__((annotate(R"ATTRDUMP(Generic binning specification)ATTRDUMP"))) __attribute__((annotate("$clingAutoload$esroofit/RooNonCentralBinning.h")))  RooNonCentralBinning;
class __attribute__((annotate("$clingAutoload$esroofit/RooTruncExponential.h")))  RooTruncExponential;
class __attribute__((annotate("$clingAutoload$esroofit/RooWeibull.h")))  RooWeibull;
class __attribute__((annotate("$clingAutoload$esroofit/TMsgLogger.h")))  TMsgLogger;
)DICTFWDDCLS";
    static const char* payloadCode = R"DICTPAYLOAD(
#line 1 "libesroofit dictionary payload"

#ifndef G__VECTOR_HAS_CLASS_ITERATOR
  #define G__VECTOR_HAS_CLASS_ITERATOR 1
#endif

#define _BACKWARD_BACKWARD_WARNING_H
#include "esroofit/ABCDUtils.h"
#include "esroofit/DataUtils.h"
#include "esroofit/DrawUtils.h"
#include "esroofit/RhhNDKeysPdf.h"
#include "esroofit/RooABCDHistPdf.h"
#include "esroofit/RooBurr.h"
#include "esroofit/RooComplementCoef.h"
#include "esroofit/RooExpandedFitResult.h"
#include "esroofit/RooNonCentralBinning.h"
#include "esroofit/RooParamHistPdf.h"
#include "esroofit/RooTruncExponential.h"
#include "esroofit/RooWeibull.h"
#include "esroofit/Statistics.h"
#include "esroofit/TMsgLogger.h"

#undef  _BACKWARD_BACKWARD_WARNING_H
)DICTPAYLOAD";
    static const char* classesHeaders[]={
"RhhNDKeysPdf", payloadCode, "@",
"RooABCDHistPdf", payloadCode, "@",
"RooBurr", payloadCode, "@",
"RooComplementCoef", payloadCode, "@",
"RooExpandedFitResult", payloadCode, "@",
"RooNonCentralBinning", payloadCode, "@",
"RooParamHistPdf", payloadCode, "@",
"RooTruncExponential", payloadCode, "@",
"RooWeibull", payloadCode, "@",
"TMsgLogger", payloadCode, "@",
nullptr};

    static bool isInitialized = false;
    if (!isInitialized) {
      TROOT::RegisterModule("libesroofit",
        headers, includePaths, payloadCode, fwdDeclCode,
        TriggerDictionaryInitialization_libesroofit_Impl, {}, classesHeaders);
      isInitialized = true;
    }
  }
  static struct DictInit {
    DictInit() {
      TriggerDictionaryInitialization_libesroofit_Impl();
    }
  } __TheDictionaryInitializer;
}
void TriggerDictionaryInitialization_libesroofit() {
  TriggerDictionaryInitialization_libesroofit_Impl();
}
