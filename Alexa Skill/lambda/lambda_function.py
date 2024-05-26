# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        try:
            with open("presentacion.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Bienvenido. Puedes decir 'Hola' o 'Ayuda'. ¿Qué te gustaría probar?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class InformacionIntentHandler(AbstractRequestHandler):
    """Handler for Informacion Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("InformacionIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("informacion.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class AdmisionIntentHandler(AbstractRequestHandler):
    """Handler for Admision Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AdmisionIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("admision.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class NoticiasIntentHandler(AbstractRequestHandler):
    """Handler for Noticias Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("NoticiasIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("noticias.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."        

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class OfertaEducativaIntentHandler(AbstractRequestHandler):
    """Handler for Oferta Educativa Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("OfertaEducativaIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("ofertaeducativa.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class EducacionSecundariaObligatoriaIntentHandler(AbstractRequestHandler):
    """Handler for Educación Secundaria Obligatoria Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("EducacionSecundariaObligatoriaIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("eso.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class BachilleratoIntentHandler(AbstractRequestHandler):
    """Handler for Bachillerato Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("BachilleratoIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("bachillerato.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FormacionProfesionalIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FormacionProfesionalIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fp.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FormacionProfesionalBasicaIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Basica Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FormacionProfesionalBasicaIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpbasica.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

        # Obtener el intent actual
        intent_name = ask_utils.get_intent_name(handler_input)

        # Verificar si el intent es FPBElectricidadIntent
        if intent_name == "FPBElectricidadIntent":
            return FPBElectricidadIntentHandler().handle(handler_input)

        # Verificar si el intent es FPBAdminGestionIntent
        elif intent_name == "FPBAdminGestionIntent":
            return FPBAdminGestionIntentHandler().handle(handler_input)

        # Si no es ninguno de los intents anteriores, se utiliza el mensaje predeterminado
        else:
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

class FPBElectricidadIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Básica en Electricidad y Electronica Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPBElectricidadIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpb_ee.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FPBAdminGestionIntentHandler(AbstractRequestHandler):
    """Handler for  Formacion Profesional Básica en Administracion y gestion Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPBAdminGestionIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpb_ag.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FormacionProfesionalMediaIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Media Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FormacionProfesionalMediaIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpmedia.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

        
        intent_name = ask_utils.get_intent_name(handler_input)

        if intent_name == "FPMSMicroRedesIntent":
            return FPMSMicroRedesIntentHandler().handle(handler_input)

        
        elif intent_name == "FPMAdminGestionIntent":
            return FPMAdminGestionIntentHandler().handle(handler_input)
        
        elif intent_name == "FPMInstalacionesElectricasIntent":
            return FPMInstalacionesElectricasIntentHandler().handle(handler_input)

        
        else:
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

class FPMSMicroRedesIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Media Sistemas Microinformaticos y Redes Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPMSMicroRedesIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpm_smr.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FPMAdminGestionIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Media Administracion y gestion Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPMAdminGestionIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpm_ag.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FPMInstalacionesElectricasIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Media Instalaciones electricas y automaticas Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPMInstalacionesElectricasIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpm_ie.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FormacionProfesionalSuperiorIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Superior Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FormacionProfesionalSuperiorIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fpsuperior.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

        intent_name = ask_utils.get_intent_name(handler_input)

        if intent_name == "FPSEnseAnimSociodeportivaIntent":
            return FPSEnseAnimSociodeportivaIntentHandler().handle(handler_input)

        elif intent_name == "FPSAdminFinanzasIntent":
            return FPSAdminFinanzasIntentHandler().handle(handler_input)
        
        elif intent_name == "FPSDesarrolloWebIntent":
            return FPSDesarrolloWebIntentHandler().handle(handler_input)
        
        elif intent_name == "FPSDesarrolloMultiIntent":
            return FPSDesarrolloMultiIntentHandler().handle(handler_input)

        else:
            return (
                handler_input.response_builder
                    .speak(speak_output)
                    .ask(speak_output)
                    .response
            )

class FPSEnseAnimSociodeportivaIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Superior Enseñanza y animacion sociodeportiva Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPSEnseAnimSociodeportivaIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fps_eas.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FPSAdminFinanzasIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Superior Administracion y finanzas Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPSAdminFinanzasIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fps_af.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FPSDesarrolloWebIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Superior Desarrollo de aplicaciones web Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPSDesarrolloWebIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fps_daw.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class FPSDesarrolloMultiIntentHandler(AbstractRequestHandler):
    """Handler for Formacion Profesional Superior Desarrollo de aplicaciones multiplataforma Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("FPSDesarrolloMultiIntent")(handler_input)

    def handle(self, handler_input):
        try:
            with open("fps_dam.txt", "r", encoding="utf-8") as file:
                speak_output = file.read()
        except FileNotFoundError:
            speak_output = "Lo siento, no pude encontrar información sobre eso. Por favor pruebe de nuevo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "¡Puedes saludarme! ¿Cómo puedo ayudarte?"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speak_output = "Gracias por usar la habilidad, espero que le haya servido de ayuda! Hasta la próxima!"
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, no estoy seguro. Puedes decir Hola o Ayuda. ¿Qué te gustaría hacer?"
        reprompt = "No entendí eso. ¿En qué puedo ayudarte?"
        return handler_input.response_builder.speak(speech).ask(reprompt).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "Acabas de activar " + intent_name + "."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)
        speak_output = "Lo siento, tuve problemas para hacer lo que pediste. Por favor, intenta de nuevo."
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(InformacionIntentHandler())
sb.add_request_handler(OfertaEducativaIntentHandler())
sb.add_request_handler(AdmisionIntentHandler())
sb.add_request_handler(NoticiasIntentHandler())
sb.add_request_handler(EducacionSecundariaObligatoriaIntentHandler())
sb.add_request_handler(BachilleratoIntentHandler())
sb.add_request_handler(FormacionProfesionalIntentHandler())
sb.add_request_handler(FormacionProfesionalBasicaIntentHandler())
sb.add_request_handler(FPBElectricidadIntentHandler())
sb.add_request_handler(FPBAdminGestionIntentHandler())
sb.add_request_handler(FormacionProfesionalMediaIntentHandler())
sb.add_request_handler(FPMSMicroRedesIntentHandler())
sb.add_request_handler(FPMAdminGestionIntentHandler())
sb.add_request_handler(FPMInstalacionesElectricasIntentHandler())
sb.add_request_handler(FormacionProfesionalSuperiorIntentHandler()) 
sb.add_request_handler(FPSEnseAnimSociodeportivaIntentHandler())
sb.add_request_handler(FPSAdminFinanzasIntentHandler())
sb.add_request_handler(FPSDesarrolloWebIntentHandler())
sb.add_request_handler(FPSDesarrolloMultiIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()