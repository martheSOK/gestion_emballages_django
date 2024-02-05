"use strict";
var KTUsersAddUser = (function () {
    const t = document.getElementById("kt_modal_add_user"),
        e = t.querySelector("#kt_modal_add_user_form"),
        n = new bootstrap.Modal(t);
    return {
        init: function () {
            (() => {
                var o = FormValidation.formValidation(e, {
                    fields: { user_name: { validators: { notEmpty: { message: "Le nom complet est requis" } } }, user_email: { validators: { notEmpty: { message: "Une adresse e-mail valide est requise" } } } },
                    plugins: { trigger: new FormValidation.plugins.Trigger(), bootstrap: new FormValidation.plugins.Bootstrap5({ rowSelector: ".fv-row", eleInvalidClass: "", eleValidClass: "" }) },
                });
                const i = t.querySelector('[data-kt-users-modal-action="submit"]');
                i.addEventListener("click", (t) => {
                    t.preventDefault(),
                        o &&
                            o.validate().then(function (t) {
                                console.log("Validé !"),
                                    "Valid" == t
                                        ? (i.setAttribute("data-kt-indicator", "on"),
                                          (i.disabled = !0),
                                          setTimeout(function () {
                                              i.removeAttribute("data-kt-indicator"),
                                                  (i.disabled = !1),
                                                  Swal.fire({ text: "Le formulaire a été soumis avec succès !", icon: "success", buttonsStyling: !1, confirmButtonText: "D'accord, compris !", customClass: { confirmButton: "btn btn-primary" } }).then(
                                                      function (t) {
                                                          t.isConfirmed && n.hide();
                                                      }
                                                  );
                                          }, 2e3))
                                        : Swal.fire({
                                              text: "Désolé, il semble y avoir des erreurs détectées, veuillez réessayer.",
                                              icon: "error",
                                              buttonsStyling: !1,
                                              confirmButtonText: "D'accord, compris !",
                                              customClass: { confirmButton: "btn btn-primary" },
                                          });
                            });
                }),
                    t.querySelector('[data-kt-users-modal-action="cancel"]').addEventListener("click", (t) => {
                        t.preventDefault(),
                            Swal.fire({
                                text: "Êtes-vous sûr de vouloir annuler ?",
                                icon: "warning",
                                showCancelButton: !0,
                                buttonsStyling: !1,
                                confirmButtonText: "Oui, annulez !",
                                cancelButtonText: "Non, retour",
                                customClass: { confirmButton: "btn btn-primary", cancelButton: "btn btn-active-light" },
                            }).then(function (t) {
                                t.value
                                    ? (e.reset(), n.hide())
                                    : "cancel" === t.dismiss &&
                                      Swal.fire({ text: "Votre formulaire n'a pas été annulé !", icon: "error", buttonsStyling: !1, confirmButtonText: "D'accord, compris !", customClass: { confirmButton: "btn btn-primary" } });
                            });
                    }),
                    t.querySelector('[data-kt-users-modal-action="close"]').addEventListener("click", (t) => {
                        t.preventDefault(),
                            Swal.fire({
                                text: "Êtes-vous sûr de vouloir annuler ?",
                                icon: "warning",
                                showCancelButton: !0,
                                buttonsStyling: !1,
                                confirmButtonText: "Oui, annulez !",
                                cancelButtonText: "Non, retour",
                                customClass: { confirmButton: "btn btn-primary", cancelButton: "btn btn-active-light" },
                            }).then(function (t) {
                                t.value
                                    ? (e.reset(), n.hide())
                                    : "cancel" === t.dismiss &&
                                      Swal.fire({ text: "Votre formulaire n'a pas été annulé !", icon: "error", buttonsStyling: !1, confirmButtonText: "D'accord, compris !", customClass: { confirmButton: "btn btn-primary" } });
                            });
                    });
            })();
        },
    };
})();
KTUtil.onDOMContentLoaded(function () {
    KTUsersAddUser.init();
});






    function updateFormAction(EmployeId) {
        var form = document.getElementById('kt_modal_add_user_form');
        var url = "/caisse/update_admin/"+EmployeId+"/";
    
        
        form.action = url;
    }


