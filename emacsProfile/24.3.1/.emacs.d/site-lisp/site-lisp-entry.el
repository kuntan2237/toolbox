;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; Kun's Emacs Profile
;;; Site LIST Entry
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; ==========Compare Directory==========
;; https://github.com/fourier/ztree.git
(add-to-list 'load-path' "~/.emacs.d/ztree")
(require 'ztree)

;; ==========Load xcscope=========
;; https://github.com/dkogan/xcscope.el.git
(add-to-list 'load-path' "~/.emacs.d/xcscope.el")
(require 'xcscope)
    (define-key global-map [(control f1)]  'cscope-set-initial-directory)
    (define-key global-map [(control f2)]  'cscope-unset-initial-directory)
(cscope-setup)

(provide 'site-lisp-entry)
